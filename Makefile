include .env

ifeq ($(OS),Windows_NT) 
    detected_OS := Windows
	VENV_BIN_DIR = venv/Scripts
	PYTHON = "$(VENV_BIN_DIR)/python.exe"
else
    detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
	VENV_BIN_DIR = venv/bin
	PYTHON = "$(VENV_BIN_DIR)/python3"
endif

CMD_FROM_VENV = ". $(VENV_BIN_DIR)/activate; which"
PIP = "$(VENV_BIN_DIR)/pip"
define create-venv
$(PYTHON_ROOT)/python3 -m venv venv
endef
define create-venv-win
$(PYTHON_ROOT)/python.exe -m venv venv
endef

.PHONY: all
all: run-py

run-py:
	@$(PYTHON) engineering/sfd1.py

run-py1:
	@$(PYTHON) airplane-forward-motion/python_parabola.py

run-py2:
	@$(PYTHON) free-fall-motion/python_Earth_Mars_Moon.py

run-py3:
	@$(PYTHON) oscillation/python_sinusoidal_motion.py

run-py4:
	@$(PYTHON) watertank/python_waterTanks.py

run-py5:
	@$(PYTHON) 2d-motion/python_2D_motion.py

run-py6:
	@$(PYTHON) 3d-motion/python_3D_motion.py

run-py7:
	@$(PYTHON) robot/python_robot.py

run-py8:
	@$(PYTHON) pid-train/python_pid_train.py

run-py9:
	@$(PYTHON) autonomous-vehicle/MAIN_MPC_car_lateral.py

run-py10:
	@$(PYTHON) drone/python_3D_motion_drone.py

venv:
	@$(create-venv)
	@$(PIP) install -r requirements.txt

venv-win:
	@$(create-venv-win)
	@$(PIP) install -r requirements.txt

clean-venv:
	@rm -rf venv