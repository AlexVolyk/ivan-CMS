from .set_main import set_main
from .main_price_info_R_S import main_price_info_R_S
from .minor_price_info_U_V_W import minor_price_info_U_V_W
from .minor_info_Y_Z import minor_info_Y_Z


def init_fields_data(
        sh,
        mode,
        data,
        date,
        main_head_style,
        profit_style,
        actual_profit_style,
        sold_status_style,
        not_sold_status_style,
        new_state_style,
        good_state_style,
        damaged_state_style,
        used_state_style
):

        set_main(
                sh,
                mode,
                data,
                main_head_style,
                sold_status_style,
                not_sold_status_style,
                new_state_style,
                good_state_style,
                damaged_state_style,
                used_state_style
        )
        main_price_info_R_S(
                sh,
                mode,
                data,
                profit_style,
                actual_profit_style
        )
        minor_price_info_U_V_W(
                sh,
                mode,
                data
        )
        minor_info_Y_Z(
                sh,
                mode,
                data,
                date
        )
