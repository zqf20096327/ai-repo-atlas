# licyk/term-sd

⭐ 29 · Shell · GPL-3.0 · 推送 2026-05-25 · [GitHub](https://github.com/licyk/term-sd) · 个人维护 · 中文 README

**基于 Dialog 的 AI 绘图软件安装与管理器（Bash 脚本）**

Term-SD 是用 Bash 编写、以 Dialog 作为终端前端界面的 AI 软件管理器，支持在 Linux/Windows/macOS 上安装和管理 Stable-Diffusion-WebUI 及其变体、ComfyUI、InvokeAI、Fooocus、lora-scripts、kohya_ss 等软件。通过下载 term-sd.sh 单脚本启动，可自定义安装路径、指定 Python 解释器路径、创建快捷命令。README 声明该项目已不再功能维护，由 licyk/sd-webui-all-in-one-launcher 接替。Windows 需 MSYS2 环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单脚本 aria2c 下载即可启动使用
- 支持安装管理 SD-WebUI 系/ComfyUI/InvokeAI/Fooocus/kohya_ss 等
- 跨 Linux/Windows/macOS，支持自定义安装路径与指定 Python 路径
- 提供国内 Gitee 仓库与 MSYS2/Homebrew 清华镜像下载途径

## 适用场景

- 一键安装并管理多个 Stable Diffusion 生态软件
- 为不同 AI 软件配置独立的 Python 运行环境
- 国内网络环境下通过镜像源部署 AI 绘图软件

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L11: Term-SD 是一款基于 Dialog 实现前端界面显示的 AI 管理器，支持安装，管理以下软件：
> L12: - 1、Stable-Diffusion-WebUI / Stable-Diffusion-WebUI-Forge / stable-diffusion-webui-reForge / Stable-Diffusion-WebUI
> L16: - 5、lora-scripts

## 星数曲线

```mermaid
xychart-beta
    title "licyk/term-sd 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `fecb1612f037` · [字段定义](../../DATASET.md)*
