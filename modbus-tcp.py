# coding:utf-8
import codecs

import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time

client = mqtt.Client()
client.username_pw_set("eiJ6hdRPHmPh5hxmZ5ld"," ")
client.connect("thingsboard.cloud", 1883, 60)


if __name__ == '__main__':
    while True:
        MainSystem_01 = {"MainSystemPower" : 11, 
                         "MainGridPower":12, 
                         "MainChargingPower" : 13, 
                         "MainMPPTPower" : 14,
                         "MainTotalGreenEnergy" : 15,
                         "MainCarbonRedcing" : 16,
                         "MainWindMPPTPower" : 17,
                         "MainTodayGreenEnergy" : 18,
                         "MainBatterySOC" : 19,
                         "AmbientTemperature" : 20,
                         "PVMPPTPower" : 21                  
                         }
        InverterRPhase01 = {"RP01GridvoltageAC_1" : 11, 
                            "RP01GridcurrentAC_1":12, 
                            "RP01GridWattAC_1" : 13, 
                            "RP01GridFrequency_1" : 14,
                            "RP01ProtectLoadVoltage_1" : 15,
                            "RP01ProtectLoadcurrent_1" : 16,
                            "RP01ProtectLoadWatt_1" : 17,
                            "RP01ProtectLoadFrequency_1" : 18,
                            "RP01InverterLoadVoltage_1" : 19,
                            "RP01InverterLoadcurrent_1" : 20,
                            "RP01InverterWatt_1" : 21,
                            "RP01InverterFrequency_1" : 22,
                            "RP01GridvoltageAC_2" : 11, 
                            "RP01GridcurrentAC_2":12, 
                            "RP01GridWattAC_2" : 13, 
                            "RP01GridFrequency_2" : 14,
                            "RP01ProtectLoadVoltage_2" : 15,
                            "RP01ProtectLoadcurrent_2" : 16,
                            "RP01ProtectLoadWatt_2" : 17,
                            "RP01ProtectLoadFrequency_2" : 18,
                            "RP01InverterLoadVoltage_2" : 19,
                            "RP01InverterLoadcurrent_2" : 20,
                            "RP01InverterWatt_2" : 21,
                            "RP01InverterFrequency_2" : 22,
                            "RP01Inverterinternaltemperature" : 23,
                            "RP01WorkingMode" : 23,
                            "RP01BatteryVoltage" : 23,
                            "RP01Batterytemperature" : 23,
                            "RP01BatteryCharging current" : 23,
                            "RP01BatteryDischarging current" : 23,
                            "RP01Batterystatus" : 23,
                            "RP011stinputvoltageDC" : 23,
                            "RP011stinputcurrentDC" : 23,
                            "RP011stinputpower Low Word" : 23,
                            "RP012ndinputvoltageDC" : 23,
                            "RP012ndinputcurrentDC" : 23,
                            "RP012ndinputpower" : 23,
                            "RP01ErrorCode1" : 23,
                            "RP01LocalLoadtotal" : 23,
                            "RP01GridPowertotal" : 23,
                            "RP01PVPowertotal" : 23
                            }
        InverterSPhase01 = {"SP01GridvoltageAC_1" : 11, 
                            "SP01GridcurrentAC_1":12, 
                            "SP01GridWattAC_1" : 13, 
                            "SP01GridFrequency_1" : 14,
                            "SP01ProtectLoadVoltage_1" : 15,
                            "SP01ProtectLoadcurrent_1" : 16,
                            "SP01ProtectLoadWatt_1" : 17,
                            "SP01ProtectLoadFrequency_1" : 18,
                            "SP01InverterLoadVoltage_1" : 19,
                            "SP01InverterLoadcurrent_1" : 20,
                            "SP01InverterWatt_1" : 21,
                            "SP01InverterFrequency_1" : 22,
                            "SP01GridvoltageAC_2" : 11, 
                            "SP01GridcurrentAC_2":12, 
                            "SP01GridWattAC_2" : 13, 
                            "SP01GridFrequency_2" : 14,
                            "SP01ProtectLoadVoltage_2" : 15,
                            "SP01ProtectLoadcurrent_2" : 16,
                            "SP01ProtectLoadWatt_2" : 17,
                            "SP01ProtectLoadFrequency_2" : 18,
                            "SP01InverterLoadVoltage_2" : 19,
                            "SP01InverterLoadcurrent_2" : 20,
                            "SP01InverterWatt_2" : 21,
                            "SP01InverterFrequency_2" : 22,
                            "SP01Inverterinternaltemperature" : 23,
                            "SP01WorkingMode" : 23,
                            "SP01BatteryVoltage" : 23,
                            "SP01Batterytemperature" : 23,
                            "SP01BatteryCharging current" : 23,
                            "SP01BatteryDischarging current" : 23,
                            "SP01Batterystatus" : 23,
                            "SP011stinputvoltageDC" : 23,
                            "SP011stinputcurrentDC" : 23,
                            "SP011stinputpower Low Word" : 23,
                            "SP012ndinputvoltageDC" : 23,
                            "SP012ndinputcurrentDC" : 23,
                            "SP012ndinputpower" : 23,
                            "SP01ErrorCode1" : 23,
                            "SP01LocalLoadtotal" : 23,
                            "SP01GridPowertotal" : 23,
                            "SP01PVPowertotal" : 23
                            }
        InverterTPhase01 = {"TP01GridvoltageAC_1" : 11, 
                            "TP01GridcurrentAC_1":12, 
                            "TP01GridWattAC_1" : 13, 
                            "TP01GridFrequency_1" : 14,
                            "TP01ProtectLoadVoltage_1" : 15,
                            "TP01ProtectLoadcurrent_1" : 16,
                            "TP01ProtectLoadWatt_1" : 17,
                            "TP01ProtectLoadFrequency_1" : 18,
                            "TP01InverterLoadVoltage_1" : 19,
                            "TP01InverterLoadcurrent_1" : 20,
                            "TP01InverterWatt_1" : 21,
                            "TP01InverterFrequency_1" : 22,
                            "TP01GridvoltageAC_2" : 11, 
                            "TP01GridcurrentAC_2":12, 
                            "TP01GridWattAC_2" : 13, 
                            "TP01GridFrequency_2" : 14,
                            "TP01ProtectLoadVoltage_2" : 15,
                            "TP01ProtectLoadcurrent_2" : 16,
                            "TP01ProtectLoadWatt_2" : 17,
                            "TP01ProtectLoadFrequency_2" : 18,
                            "TP01InverterLoadVoltage_2" : 19,
                            "TP01InverterLoadcurrent_2" : 20,
                            "TP01InverterWatt_2" : 21,
                            "TP01InverterFrequency_2" : 22,
                            "TP01Inverterinternaltemperature" : 23,
                            "TP01WorkingMode" : 23,
                            "TP01BatteryVoltage" : 23,
                            "TP01Batterytemperature" : 23,
                            "TP01BatteryCharging current" : 23,
                            "TP01BatteryDischarging current" : 23,
                            "TP01Batterystatus" : 23,
                            "TP011stinputvoltageDC" : 23,
                            "TP011stinputcurrentDC" : 23,
                            "TP011stinputpower Low Word" : 23,
                            "TP012ndinputvoltageDC" : 23,
                            "TP012ndinputcurrentDC" : 23,
                            "TP012ndinputpower" : 23,
                            "TP01ErrorCode1" : 23,
                            "TP01LocalLoadtotal" : 23,
                            "TP01GridPowertotal" : 23,
                            "TP01PVPowertotal" : 23
                            }
        InverterRPhase02 = {"RP02GridvoltageAC_1" : 11, 
                         "RP02GridcurrentAC_1":12, 
                         "RP02GridWattAC_1" : 13, 
                         "RP02GridFrequency_1" : 14,
                         "RP02ProtectLoadVoltage_1" : 15,
                         "RP02ProtectLoadcurrent_1" : 16,
                         "RP02ProtectLoadWatt_1" : 17,
                         "RP02ProtectLoadFrequency_1" : 18,
                         "RP02InverterLoadVoltage_1" : 19,
                         "RP02InverterLoadcurrent_1" : 20,
                         "RP02InverterWatt_1" : 21,
                         "RP02InverterFrequency_1" : 22,
                         "RP02GridvoltageAC_2" : 11, 
                         "RP02GridcurrentAC_2":12, 
                         "RP02GridWattAC_2" : 13, 
                         "RP02GridFrequency_2" : 14,
                         "RP02ProtectLoadVoltage_2" : 15,
                         "RP02ProtectLoadcurrent_2" : 16,
                         "RP02ProtectLoadWatt_2" : 17,
                         "RP02ProtectLoadFrequency_2" : 18,
                         "RP02InverterLoadVoltage_2" : 19,
                         "RP02InverterLoadcurrent_2" : 20,
                         "RP02InverterWatt_2" : 21,
                         "RP02InverterFrequency_2" : 22,
                         "RP02Inverterinternaltemperature" : 23,
                         "RP02WorkingMode" : 23,
                         "RP02BatteryVoltage" : 23,
                         "RP02Batterytemperature" : 23,
                         "RP02BatteryCharging current" : 23,
                         "RP02BatteryDischarging current" : 23,
                         "RP02Batterystatus" : 23,
                         "RP021stinputvoltageDC" : 23,
                         "RP021stinputcurrentDC" : 23,
                         "RP021stinputpower Low Word" : 23,
                         "RP022ndinputvoltageDC" : 23,
                         "RP022ndinputcurrentDC" : 23,
                         "RP022ndinputpower" : 23,
                         "RP02ErrorCode1" : 23,
                         "RP02LocalLoadtotal" : 23,
                         "RP02GridPowertotal" : 23,
                         "RP02PVPowertotal" : 23
                         }
        InverterSPhase02 = {"SP02GridvoltageAC_1" : 11, 
                         "SP02GridcurrentAC_1":12, 
                         "SP02GridWattAC_1" : 13, 
                         "SP02GridFrequency_1" : 14,
                         "SP02ProtectLoadVoltage_1" : 15,
                         "SP02ProtectLoadcurrent_1" : 16,
                         "SP02ProtectLoadWatt_1" : 17,
                         "SP02ProtectLoadFrequency_1" : 18,
                         "SP02InverterLoadVoltage_1" : 19,
                         "SP02InverterLoadcurrent_1" : 20,
                         "SP02InverterWatt_1" : 21,
                         "SP02InverterFrequency_1" : 22,
                         "SP02GridvoltageAC_2" : 11, 
                         "SP02GridcurrentAC_2":12, 
                         "SP02GridWattAC_2" : 13, 
                         "SP02GridFrequency_2" : 14,
                         "SP02ProtectLoadVoltage_2" : 15,
                         "SP02ProtectLoadcurrent_2" : 16,
                         "SP02ProtectLoadWatt_2" : 17,
                         "SP02ProtectLoadFrequency_2" : 18,
                         "SP02InverterLoadVoltage_2" : 19,
                         "SP02InverterLoadcurrent_2" : 20,
                         "SP02InverterWatt_2" : 21,
                         "SP02InverterFrequency_2" : 22,
                         "SP02Inverterinternaltemperature" : 23,
                         "SP02WorkingMode" : 23,
                         "SP02BatteryVoltage" : 23,
                         "SP02Batterytemperature" : 23,
                         "SP02BatteryCharging current" : 23,
                         "SP02BatteryDischarging current" : 23,
                         "SP02Batterystatus" : 23,
                         "SP021stinputvoltageDC" : 23,
                         "SP021stinputcurrentDC" : 23,
                         "SP021stinputpower Low Word" : 23,
                         "SP022ndinputvoltageDC" : 23,
                         "SP022ndinputcurrentDC" : 23,
                         "SP022ndinputpower" : 23,
                         "SP02ErrorCode1" : 23,
                         "SP02LocalLoadtotal" : 23,
                         "SP02GridPowertotal" : 23,
                         "SP02PVPowertotal" : 23
                         }
        InverterTPhase02 = {"TP02GridvoltageAC_1" : 11, 
                         "TP02GridcurrentAC_1":12, 
                         "TP02GridWattAC_1" : 13, 
                         "TP02GridFrequency_1" : 14,
                         "TP02ProtectLoadVoltage_1" : 15,
                         "TP02ProtectLoadcurrent_1" : 16,
                         "TP02ProtectLoadWatt_1" : 17,
                         "TP02ProtectLoadFrequency_1" : 18,
                         "TP02InverterLoadVoltage_1" : 19,
                         "TP02InverterLoadcurrent_1" : 20,
                         "TP02InverterWatt_1" : 21,
                         "TP02InverterFrequency_1" : 22,
                         "TP02GridvoltageAC_2" : 11, 
                         "TP02GridcurrentAC_2":12, 
                         "TP02GridWattAC_2" : 13, 
                         "TP02GridFrequency_2" : 14,
                         "TP02ProtectLoadVoltage_2" : 15,
                         "TP02ProtectLoadcurrent_2" : 16,
                         "TP02ProtectLoadWatt_2" : 17,
                         "TP02ProtectLoadFrequency_2" : 18,
                         "TP02InverterLoadVoltage_2" : 19,
                         "TP02InverterLoadcurrent_2" : 20,
                         "TP02InverterWatt_2" : 21,
                         "TP02InverterFrequency_2" : 22,
                         "TP02Inverterinternaltemperature" : 23,
                         "TP02WorkingMode" : 23,
                         "TP02BatteryVoltage" : 23,
                         "TP02Batterytemperature" : 23,
                         "TP02BatteryCharging current" : 23,
                         "TP02BatteryDischarging current" : 23,
                         "TP02Batterystatus" : 23,
                         "TP021stinputvoltageDC" : 23,
                         "TP021stinputcurrentDC" : 23,
                         "TP021stinputpower Low Word" : 23,
                         "TP022ndinputvoltageDC" : 23,
                         "TP022ndinputcurrentDC" : 23,
                         "TP022ndinputpower" : 23,
                         "TP02ErrorCode1" : 23,
                         "TP02LocalLoadtotal" : 23,
                         "TP02GridPowertotal" : 23,
                         "TP02PVPowertotal" : 23
                         }
        InverterRPhase03 = {"RP03GridvoltageAC_1" : 11, 
                         "RP03GridcurrentAC_1":12, 
                         "RP03GridWattAC_1" : 13, 
                         "RP03GridFrequency_1" : 14,
                         "RP03ProtectLoadVoltage_1" : 15,
                         "RP03ProtectLoadcurrent_1" : 16,
                         "RP03ProtectLoadWatt_1" : 17,
                         "RP03ProtectLoadFrequency_1" : 18,
                         "RP03InverterLoadVoltage_1" : 19,
                         "RP03InverterLoadcurrent_1" : 20,
                         "RP03InverterWatt_1" : 21,
                         "RP03InverterFrequency_1" : 22,
                         "RP03GridvoltageAC_2" : 11, 
                         "RP03GridcurrentAC_2":12, 
                         "RP03GridWattAC_2" : 13, 
                         "RP03GridFrequency_2" : 14,
                         "RP03ProtectLoadVoltage_2" : 15,
                         "RP03ProtectLoadcurrent_2" : 16,
                         "RP03ProtectLoadWatt_2" : 17,
                         "RP03ProtectLoadFrequency_2" : 18,
                         "RP03InverterLoadVoltage_2" : 19,
                         "RP03InverterLoadcurrent_2" : 20,
                         "RP03InverterWatt_2" : 21,
                         "RP03InverterFrequency_2" : 22,
                         "RP03Inverterinternaltemperature" : 23,
                         "RP03WorkingMode" : 23,
                         "RP03BatteryVoltage" : 23,
                         "RP03Batterytemperature" : 23,
                         "RP03BatteryCharging current" : 23,
                         "RP03BatteryDischarging current" : 23,
                         "RP03Batterystatus" : 23,
                         "RP031stinputvoltageDC" : 23,
                         "RP031stinputcurrentDC" : 23,
                         "RP031stinputpower Low Word" : 23,
                         "RP032ndinputvoltageDC" : 23,
                         "RP032ndinputcurrentDC" : 23,
                         "RP032ndinputpower" : 23,
                         "RP03ErrorCode1" : 23,
                         "RP03LocalLoadtotal" : 23,
                         "RP03GridPowertotal" : 23,
                         "RP03PVPowertotal" : 23
                         }
        InverterSPhase03 = {"SP03GridvoltageAC_1" : 11, 
                         "SP03GridcurrentAC_1":12, 
                         "SP03GridWattAC_1" : 13, 
                         "SP03GridFrequency_1" : 14,
                         "SP03ProtectLoadVoltage_1" : 15,
                         "SP03ProtectLoadcurrent_1" : 16,
                         "SP03ProtectLoadWatt_1" : 17,
                         "SP03ProtectLoadFrequency_1" : 18,
                         "SP03InverterLoadVoltage_1" : 19,
                         "SP03InverterLoadcurrent_1" : 20,
                         "SP03InverterWatt_1" : 21,
                         "SP03InverterFrequency_1" : 22,
                         "SP03GridvoltageAC_2" : 11, 
                         "SP03GridcurrentAC_2":12, 
                         "SP03GridWattAC_2" : 13, 
                         "SP03GridFrequency_2" : 14,
                         "SP03ProtectLoadVoltage_2" : 15,
                         "SP03ProtectLoadcurrent_2" : 16,
                         "SP03ProtectLoadWatt_2" : 17,
                         "SP03ProtectLoadFrequency_2" : 18,
                         "SP03InverterLoadVoltage_2" : 19,
                         "SP03InverterLoadcurrent_2" : 20,
                         "SP03InverterWatt_2" : 21,
                         "SP03InverterFrequency_2" : 22,
                         "SP03Inverterinternaltemperature" : 23,
                         "SP03WorkingMode" : 23,
                         "SP03BatteryVoltage" : 23,
                         "SP03Batterytemperature" : 23,
                         "SP03BatteryCharging current" : 23,
                         "SP03BatteryDischarging current" : 23,
                         "SP03Batterystatus" : 23,
                         "SP031stinputvoltageDC" : 23,
                         "SP031stinputcurrentDC" : 23,
                         "SP031stinputpower Low Word" : 23,
                         "SP032ndinputvoltageDC" : 23,
                         "SP032ndinputcurrentDC" : 23,
                         "SP032ndinputpower" : 23,
                         "SP03ErrorCode1" : 23,
                         "SP03LocalLoadtotal" : 23,
                         "SP03GridPowertotal" : 23,
                         "SP03PVPowertotal" : 23
                         }
        InverterTPhase03 = {"TP03GridvoltageAC_1" : 11, 
                         "TP03GridcurrentAC_1":12, 
                         "TP03GridWattAC_1" : 13, 
                         "TP03GridFrequency_1" : 14,
                         "TP03ProtectLoadVoltage_1" : 15,
                         "TP03ProtectLoadcurrent_1" : 16,
                         "TP03ProtectLoadWatt_1" : 17,
                         "TP03ProtectLoadFrequency_1" : 18,
                         "TP03InverterLoadVoltage_1" : 19,
                         "TP03InverterLoadcurrent_1" : 20,
                         "TP03InverterWatt_1" : 21,
                         "TP03InverterFrequency_1" : 22,
                         "TP03GridvoltageAC_2" : 11, 
                         "TP03GridcurrentAC_2":12, 
                         "TP03GridWattAC_2" : 13, 
                         "TP03GridFrequency_2" : 14,
                         "TP03ProtectLoadVoltage_2" : 15,
                         "TP03ProtectLoadcurrent_2" : 16,
                         "TP03ProtectLoadWatt_2" : 17,
                         "TP03ProtectLoadFrequency_2" : 18,
                         "TP03InverterLoadVoltage_2" : 19,
                         "TP03InverterLoadcurrent_2" : 20,
                         "TP03InverterWatt_2" : 21,
                         "TP03InverterFrequency_2" : 22,
                         "TP03Inverterinternaltemperature" : 23,
                         "TP03WorkingMode" : 23,
                         "TP03BatteryVoltage" : 23,
                         "TP03Batterytemperature" : 23,
                         "TP03BatteryCharging current" : 23,
                         "TP03BatteryDischarging current" : 23,
                         "TP03Batterystatus" : 23,
                         "TP031stinputvoltageDC" : 23,
                         "TP031stinputcurrentDC" : 23,
                         "TP031stinputpower Low Word" : 23,
                         "TP032ndinputvoltageDC" : 23,
                         "TP032ndinputcurrentDC" : 23,
                         "TP032ndinputpower" : 23,
                         "TP03ErrorCode1" : 23,
                         "TP03LocalLoadtotal" : 23,
                         "TP03GridPowertotal" : 23,
                         "TP0PVPowertotal" : 23
                         }
        InverterOperationParameter = {"Show_ac_output_power_1" : 24,
                                      "Show_protec_load_voltage" : 24,
                                      "Show_power_factor_control" : 24,
                                      "Show_hybrid_mode" : 24,
                                      "Show_ac_output_power_2" : 24,
                                      "Show_ac_charge_mode" : 24,
                                      "Show_dry_contact_status" : 24,
                                      "Show_set_battery_parameter" : 24,
                                      "Show_number_battery_string" : 24,
                                      "Show_charge_max_amp" : 24,
                                      "Show_charge_volt_max" : 24,
                                      "Show_charge_volt_float" : 24,
                                      "Show_over_voltage" : 24,
                                      "Show_low_voltage" : 24,
                                      "Show_temperature_compensation" : 24,
                                      "Show_safty_read_status" : 24,
                                      "Show_grid_connect_time" : 24,
                                      "Show_write_battery_reserve" : 24,
                                      "Show_max_frequency_range" : 24,
                                      "Show_min_frequency_range" : 24,
                                      "Show_max_voltage_range" : 24,
                                      "Show_min_voltage_range" : 24,
                                      "Show_max_grid_voltage_10_min_moving_range" : 24
                         }
        AutoOperationParameter = {"mode_select" : 24,
                                  "mode_sell_start_voltage" : 24,
                                  "mode_sell_stop_voltage" : 24,
                                  "mode_sell_ratio" : 24,
                                  "mode_MPPT_max_voltage" : 24,
                                  "mode_MPPT_min_voltage" : 24,
                                  "mode_MPPT_charge_power" : 24,
                                  "mode_time_A_hour" : 24,
                                  "mode_time_A_min" : 24,
                                  "mode_time_A_status" : 24,
                                  "mode_time_A_power_1" : 24,
                                  "mode_time_A_power_2" : 24,
                                  "mode_time_B_hour" : 24,
                                  "mode_time_B_min" : 24,
                                  "mode_time_B_status" : 24,
                                  "mode_time_B_power_1" : 24,
                                  "mode_time_B_power_2" : 24,
                                  "mode_time_C_hour" : 24,
                                  "mode_time_C_min" : 24,
                                  "mode_time_C_status" : 24,
                                  "mode_time_C_power_1" : 24,
                                  "mode_time_C_power_2" : 24,
                                  "mode_time_D_hour" : 24,
                                  "mode_time_D_min" : 24,
                                  "mode_time_D_status" : 24,
                                  "mode_time_D_power_1" : 24,
                                  "mode_time_D_power_2" : 24,
                                  "mode_executio" : 24
                                  }
        
        for i in range(90):
            pets={"BatteryID"+str(i):
                  {str(i)+"stBatterystateofcharge" : 44,
                   str(i)+"stBatteryPackWarningFlag" : 44,
                   str(i)+"stBatteryCurrent" : 44,
                   str(i)+"stBatteryVoltage" : 44,
                   str(i)+"stHighTemperature" : 44,
                   str(i)+"stSOH" : 44
                   }
                  }
            print (pets)
            client.publish("v1/devices/me/telemetry", json.dumps(pets["BatteryID"+str(i)]))
        
        
        print (json.dumps(MainSystem_01))
        client.publish("v1/devices/me/telemetry", json.dumps(MainSystem_01))
        client.publish("v1/devices/me/telemetry", json.dumps(InverterRPhase01))
        client.publish("v1/devices/me/telemetry", json.dumps(InverterSPhase01))
        client.publish("v1/devices/me/telemetry", json.dumps(InverterTPhase01))
        client.publish("v1/devices/me/telemetry", json.dumps(InverterRPhase02))
        client.publish("v1/devices/me/telemetry", json.dumps(InverterSPhase02))
        client.publish("v1/devices/me/telemetry", json.dumps(InverterTPhase03))
        client.publish("v1/devices/me/telemetry", json.dumps(InverterRPhase03))
        client.publish("v1/devices/me/telemetry", json.dumps(InverterSPhase03))
        client.publish("v1/devices/me/telemetry", json.dumps(InverterTPhase03))
        client.publish("v1/devices/me/telemetry", json.dumps(InverterOperationParameter))
        client.publish("v1/devices/me/telemetry", json.dumps(AutoOperationParameter))
        

        
        time.sleep(100)