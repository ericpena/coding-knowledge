import pandas as pd

class Task():
    """
    status:
        0: pending
        1: in_progress
        2: completed
    """
    def __init__(self, task_id, description, origin, destination):
        self.task_id = task_id
        self.description = description
        self.origin = origin
        self.destination = destination
        self.status = 0

class Vehicle():

    def __init__(self, vin, make, model, year) -> None:
        """
        status:
            0: idle
            1: in_transit
            2: maintenance
        """        
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.status = 0
        self.tasks = {}

    # :: TODO: Can I prevent this task from being called on its own outside of Fleet class using it?
    def assign_task(self, task : Task) -> None:
        self.tasks[task.task_id] = task

    def start_task(self, task : Task) -> None:
        task.status = 1
        self.status = 1
        print('Task has begun.')

    def complete_tasks(self) -> None:
        for _, task in self.tasks.items():
            task.status = 2 if task.status == 1 else task.status
        self.status = 2

    def complete_task(self, task : Task) -> None:
        self.tasks[task.task_id].status = 2 if self.tasks[task.task_id].status == 1 else self.tasks[task.task_id].status
        self.status = 2
        print('Task marked as completed.')

    def get_info(self):
        return f'vin: {self.vin}, make: {self.make}, model: {self.model}, year: {self.year}, status: {self.status}, num_tasks: {len(self.tasks)}'

class Fleet():

    def __init__(self) -> None:
        self.fleet = {}
    
    def add_vehicle(self, vehicle):
        self.fleet[vehicle.vin] = vehicle
        print(f'[{vehicle.vin}] was added to fleet.')

    def remove_vehicle(self, vehicle):
        v = self.fleet.pop(vehicle.vin, "Vehicle not in fleet.")
        print(f'[{v}] was removed from fleet.')

    def assign_task_to_vehicle(self, task, vin):
        self.fleet[vin].assign_task(task)

    def complete_vehicle_task(self, task, vin):
        self.fleet[vin].complete_task(task)

    def get_fleet_status(self) -> pd.DataFrame:
        # :: print vehicle vin, status, numbers of tasks, number of tasks in each category.
        df = pd.DataFrame(columns=('vin', 'status', 'num_tasks', 'idle_tasks', 'in_progress_tasks', 'completed_tasks'))
        for vin, veh in self.fleet.items():

            new_record = pd.DataFrame({'vin':[vin],
            'status':[veh.status],
            'num_tasks':[len(veh.tasks)],
            'idle_tasks':[sum([1 for _, t in veh.tasks.items() if t.status == 0])],
            'in_progress_tasks':[sum([1 for _, t in veh.tasks.items() if t.status == 1])],
            'completed_tasks':[sum([1 for _, t in veh.tasks.items() if t.status == 2])]})
        
            df = pd.concat([df, new_record], axis=0, ignore_index=True).reset_index(drop=True)
        
        labels = ['idle', 'in_transit', 'maintenance']
        df['status'] = [labels[i] for i in df['status']]

        return df
    
def main():
    # Example usage
    fleet = Fleet()

    # Adding vehicles
    vehicle1 = Vehicle('1HGCM82633A004352', 'Tesla', 'Model S', 2022)
    vehicle2 = Vehicle('1FTFW1E57JFA30456', 'Waymo', 'Chrysler Pacifica', 2021)

    fleet.add_vehicle(vehicle1)
    fleet.add_vehicle(vehicle2)

    # Creating tasks
    task1 = Task(1, "Deliver package", "Location A", "Location B")
    task2 = Task(2, "Pick up passenger", "Location C", "Location D")

    # Assigning tasks to vehicles
    fleet.assign_task_to_vehicle(task1, '1HGCM82633A004352')
    fleet.assign_task_to_vehicle(task2, '1FTFW1E57JFA30456')

    # Generating fleet status report
    print(fleet.get_fleet_status())

    vehicle1.start_task(task1)
    vehicle2.start_task(task2)

    # Generating fleet status report
    print(fleet.get_fleet_status())

    # Completing a task
    fleet.complete_vehicle_task(task1, '1HGCM82633A004352')

    # Generating fleet status report
    print(fleet.get_fleet_status())

if __name__ == '__main__':
    main()