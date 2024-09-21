from triplea.service.repository.pipeline_core import move_state_forward
import triplea.service.repository.pipeline_flag as cPIPELINE
import triplea.service.repository.persist as PERSIST
if __name__ == "__main__":

    # # Moving from `0` to `1`  - original details of article saved (json Form)
    # move_state_forward(0)                    

    # # Moving from `1` to `2` - parse details info of article
    # move_state_forward(1)

    # # Moving from `2` to `3` - Get Citation
    # move_state_forward(2)

    # # # Moving forward in custom pipeline

    # ### Extract Topic
    # cPIPELINE.go_extract_topic()

    # ### Affiliation Mining
    # cPIPELINE.go_affiliation_mining(method="TitipataIntegrated")

    PERSIST.refresh()