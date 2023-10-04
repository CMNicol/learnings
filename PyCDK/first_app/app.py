#!/usr/bin/env python3
import os

import aws_cdk as cdk

from first_app.first_app_stack import FirstAppStack


app = cdk.App()
FirstAppStack(app, "FirstAppStack")

app.synth()
