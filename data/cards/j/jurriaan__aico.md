# jurriaan/aico

⭐ 14 · Rust · MIT · 推送 2026-09-25 · [GitHub](https://github.com/jurriaan/aico) · 个人维护

**面向软件工程的 LLM 命令行客户端：生成可审查的代码补丁**

用 Rust 编写的 CLI 工具，将 LLM 定位为从属实现引擎：用户手动 add/drop 文件管理上下文窗口，用 ask 讨论设计、gen 生成统一 diff 格式补丁，再自行用 patch 应用。它不自主执行代码或编辑文件，输出机器可读数据到 stdout 以便与 Unix 工具组合。支持 OpenAI 直连与经 OpenRouter 接入 Claude/Gemini 等非 OpenAI 模型，通过 API key 环境变量配置；提供预编译二进制与 cargo install 两种安装方式，并支持会话分支与插件扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 显式 add/drop 文件控制上下文窗口
- ask 讨论与 gen 生成 unified diff 分离，补丁需手动 patch 应用
- 支持 OpenAI 直连与经 OpenRouter 接入非 OpenAI 模型
- 会话分支（session-fork）与 .aico/addons/ 插件扩展

## 适用场景

- 以规格驱动流程（测试先行）让 LLM 实现代码改动
- 在自主应用补丁前审查每处代码变更
- 用 CONVENTIONS.md 自定义简写指令加速日常开发

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: `aico` is an LLM client designed for the software engineering lifecycle. It treats the Large Language Model as a sub
> L5: Unlike agents that try to take over, `aico` is a "hands-on" tool. You explicitly manage the context window to define
> L11: - **It's a tool, not an agent.** `aico` does not execute code or edit files autonomously. It reads input and produc

## 星数曲线

```mermaid
xychart-beta
    title "jurriaan/aico 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c7cb8783d8ad` · [字段定义](../../DATASET.md)*
