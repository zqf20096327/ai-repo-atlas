# CursedPrograms/Image-Generator

⭐ 10 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/CursedPrograms/Image-Generator) · [官网](https://cursedprograms.github.io/Image-Generator/) · 个人维护

**基于 SDXL-Turbo 的命令行文生图与图生图工具**

Python 命令行工具，通过 SDXL-Turbo 模型提供文生图与图生图两类操作：用户选择模式、输入提示词后，脚本生成并执行对应代码片段，结果保存至 output 目录；另提供 scripts/generate.py 接口供其他程序调用，支持单次提示、批量 job 文件及切换更小的 sd-turbo 模型。安装方式为创建 Python 虚拟环境后执行 pip install -r requirements.txt，覆盖 Linux 与 Windows PowerShell。以 MIT 许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文生图与图生图两种模式的命令行交互
- scripts/generate.py 提供供其他程序调用的生成接口
- job 文件支持批量生成图片（单次模型加载）
- 可通过 --model 参数切换 sd-turbo 模型（4 GB GPU、8 GB RAM）

## 适用场景

- 在本地通过命令行将文本提示词转为图片
- 基于已有图片按提示词做图生图变换
- 从其他脚本或程序批量调用图片生成功能

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L20: This Python project provides a simple command-line interface for interacting with the SDXL-Turbo model, showcasing 
> L24: Allows users to convert a text prompt into an image using the SDXL-Turbo model.

## 星数曲线

```mermaid
xychart-beta
    title "CursedPrograms/Image-Generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `9e81fec8265d` · [字段定义](../../DATASET.md)*
