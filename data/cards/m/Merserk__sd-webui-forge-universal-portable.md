# Merserk/sd-webui-forge-universal-portable

⭐ 31 · Batchfile · MIT · 推送 2026-08-30 · [GitHub](https://github.com/Merserk/sd-webui-forge-universal-portable) · 个人维护

**SD WebUI Forge（Classic/Neo）的 Windows 全便携安装器**

面向 Windows 用户的单脚本安装器与启动器：下载 install_forge_universal.bat 放入目标文件夹双击运行，可从菜单选择安装 Forge Classic（稳定、兼容旧扩展）或 Forge Neo（实验、新特性）分支，两者可并排安装。通过 UV 管理包以缩短安装时间，内置 Embedded Python 3.13 与 MinGit，无需全局安装；Classic 分支自动安装预编译 insightface wheel。安装后生成 run/update 批处理脚本。本仓库仅提供安装器，WebUI 本体来自 Haoming02 维护的 Forge 分支。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 菜单选择安装 Forge Classic 或 Neo 分支，可并排共存
- 使用 UV 管理包，内置 Embedded Python 3.13 与 MinGit，无需全局依赖
- 自动安装预编译 insightface wheel（Classic 分支）
- 生成 run/update 批处理脚本用于启动与更新

## 适用场景

- 在 Windows 上一键安装便携版 SD WebUI Forge，无需配置 Python 环境
- 同一文件夹中并排维护 Classic 与 Neo 两个分支
- 通过 update 批处理脚本更新仓库与依赖包

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L10: A lightning-fast, zero-dependency, **fully portable** installer for SD WebUI Forge.
> L14: This script allows you to choose between the **Classic** (Stable) and **Neo** (Experimental) branches. It sets up a
> L73: **This repository provides a universal, portable installer to easily run either the Classic or Neo branch.**

## 星数曲线

```mermaid
xychart-beta
    title "Merserk/sd-webui-forge-universal-portable 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-28 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f612952ed982` · [字段定义](../../DATASET.md)*
