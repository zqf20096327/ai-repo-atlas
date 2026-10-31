# badgids/comfyui-setup-manager

⭐ 18 · Python · Apache-2.0 · 推送 2026-08-21 · [GitHub](https://github.com/badgids/comfyui-setup-manager) · [官网](https://github.com/badgids/comfyui-setup-manager) · 个人维护

**ComfyUI 安装管理器：安装、启动、更新、导出 ComfyUI 环境**

独立命令行/TUI 应用，用于安装、启动、更新、回滚、检查、导入导出与共享 ComfyUI 安装、模型与工作流。提供 Textual 终端界面与完整 CLI（输出可为 text/JSON/YAML）、可移植 YAML 配置 profile、共享外部模型与工作流库、更新快照回滚、自定义节点启动验证、工作流打包及 Agent Skills 与 MCP 定义管理。要求 Python 3.10+、Git 与网络访问；自身创建私有 venv，不需全局安装。面向管理多个 ComfyUI 实例的用户与自动化脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TUI + 完整 CLI 双界面，CLI 输出支持 text/JSON/YAML
- YAML profile 可移植导入导出，含精确重建计划
- 共享外部模型/工作流库避免多实例重复存储
- 更新带快照回滚、pip check 与启动/导入验证

## 适用场景

- 在多台机器或多个目录间迁移和复现 ComfyUI 环境
- 集中管理模型、LoRA 与工作流的共享库
- 自动化脚本批量检查和更新 ComfyUI 安装

## 场景标签

 · 领域:AI 工作流工具链管理

## 证据(README 行号)

> L7: ComfyUI Setup Manager is a standalone application for installing, launching, updating, repairing, inspecting, export
> L11: - a compact Textual terminal interface for people;
> L12: - a complete non-TUI command-line interface for scripts and automation;

## 星数曲线

```mermaid
xychart-beta
    title "badgids/comfyui-setup-manager 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3729225023d5` · [字段定义](../../DATASET.md)*
