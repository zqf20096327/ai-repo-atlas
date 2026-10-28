# ok-oldking/ok-script

⭐ 806 · Python · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/ok-oldking/ok-script) · [官网](https://ok-script.com/) · 个人维护 · 中文 README

**Python 桌面/安卓自动化框架，配 MCP 供编程代理开发脚本**

面向 Windows 应用与游戏、安卓模拟器及 ADB 设备的 Python 自动化框架：提供截图、OCR、OpenCV 模板匹配、YOLO 视觉方案、后台输入、COCO 模板管理与任务打包。通过 MCP 服务让编程代理检查已安装 API、编写并测试 Python 任务，保存后的任务可从 GUI 或命令行反复运行，无需代理或大模型调用。要求 Python 3.11+；OpenCV 需单独安装兼容变体，Qt、ADB、OCR 按需安装。采用 Apache 2.0 + Commons Clause 及附加条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一任务代码支持 Windows 客户端、安卓模拟器和 ADB 设备
- MCP 服务供编程代理检查 API、开发并测试自动化任务
- 支持 OCR、OpenCV 模板匹配及 YOLO 等视觉方案
- 基于 COCO 标注管理模板素材并按屏幕分辨率自动缩放

## 适用场景

- 开发游戏或桌面应用的自动化脚本并反复运行
- 让编程代理通过 MCP 代写和调试自动化任务
- 在国内安卓模拟器或 ADB 设备上跑视觉识别自动化

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: 把需求告诉编程代理，通过 MCP 连接 ok-script，让代理观察应用、检查已安装 API、编写并测试 Python 任务。保存成果后，从应用 GUI 或命令行重复运行，无需代理或大模型调用。
> L25: > 连接这个项目的 ok-script MCP 服务，读取开发技能。检查已安装的截图、匹配和输入 API，给出准确签名和源码位置。开发可复用 Python 任务：打开设置、启用“显示详情”、保存并验证结果。每次尝试前恢复并验证起始
> L60: 具体 Python API 由代理检查已安装包的源码和签名。MCP 提供开发技能和执行工具，没有单独的 API 查询工具。完成的任务可在无界面模式或桌面 GUI 中运行，详见运行时架构。


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `0faffe9c33f1` · [字段定义](../../DATASET.md)*
