import engine.DriveControls as Controls
import scripts.LineFollower as LineFollower
import scripts.FollowObject as FollowObject

print('1 = line follower')
print('2 = follow object')
select_script_input = int(input('Select a script:'))

Controls.stop_motors()


def choose(choice):
    if choice == 1:
        LineFollower.start()
    elif choice == 2:
        FollowObject.start()
    else:
        choose(int(input('This is not an option!')))


choose(select_script_input)
