# rookiestar28/Git-Manager-Pro

⭐ 22 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/rookiestar28/Git-Manager-Pro) · 个人维护 · 中文 README

**管理 ComfyUI 自定义节点的批量 Git 与依赖安装工具集**

面向 AIGC 工程师与 ComfyUI 使用者的脚本集，包含两个核心工具：Git Manager Pro 批量执行 custom_nodes 的 git pull 更新、非 Git 文件夹转 Git 仓库、按时间戳批量 git reset 回退；Auto Installer 从文本文件批量克隆仓库并扫描各节点 requirements.txt 批量安装 pip 依赖。支持系统 Python/venv/Conda/ComfyUI Portable 的解释器发现机制，提供 Windows 批处理与 Linux/WSL 的 sh 启动器（macOS 未验证），并支持非交互 CLI 调用与 schema 化 JSON 结果输出。需系统安装 Git，Time Machine 的 git reset --hard 会丢弃未提交更改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 批量更新/回退 custom_nodes 仓库，跳过无上游跟踪的仓库
- 非 Git 文件夹按映射列表转换为 Git 仓库
- 批量克隆与批量安装各节点 requirements.txt 依赖
- 非交互 CLI 模式与 schema 版本化的 JSON 结果输出

## 适用场景

- 一次性更新全部 ComfyUI 自定义节点
- 新环境或迁移时批量克隆节点并安装依赖
- 全局更新出问题时按时间戳批量回退节点版本

## 场景标签

 · 领域:AI 工作流工具/ComfyUI 生态

## 证据(README 行号)

> L7: Welcome to the **Git Manager Pro**. This collection of scripts is designed specifically for AIGC engineers and Comfy
> L9: For Auto Installer, whether you use system Python, a venv, Conda, or the ComfyUI Portable (Embedded)

## 星数曲线

```mermaid
xychart-beta
    title "rookiestar28/Git-Manager-Pro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `4fe577464bcf` · [字段定义](../../DATASET.md)*
