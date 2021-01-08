void app_main()
{        gpio_config_t conf = {
                .pull_down_en = 0, 
                .pull_down_en = 0, 
                .pull_up_en = 0, 
                .intr_type =  ,
                .mode = GPIO_MODE_INPUT, 
                .pin_bit_mask = , 
        };
        gpio_config(&conf);
        conf = {
                .pull_down_en = 0, 
                .pull_down_en = 0, 
                .pull_up_en = 0, 
                .intr_type = GPIO_INTR_DISABLE, 
                .mode = GPIO_MODE_INPUT, 
                .pin_bit_mask = (1ULL<<GPIO_NUM_12) , 
        };
        gpio_config(&conf);
        conf = {
                .pull_down_en = 0, 
                .pull_down_en = 0, 
                .pull_up_en = 0, 
                .intr_type = GPIO_INTR_DISABLE, 
                .mode = GPIO_MODE_OUTPUT, 
                .pin_bit_mask = (1ULL<<GPIO_NUM_4)  | (1ULL<<GPIO_NUM_0) , 
        };
        gpio_config(&conf);
        conf = {
                .pull_down_en = 0, 
                .pull_down_en = 0, 
                .pull_up_en = 0, 
                .intr_type = GPIO_INTR_POSEDGE ,
                .mode = GPIO_MODE_INPUT, 
                .pin_bit_mask = (1ULL<<GPIO_NUM_14) , 
        };
        gpio_config(&conf);
}