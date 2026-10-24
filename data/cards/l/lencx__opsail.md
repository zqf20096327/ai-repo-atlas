# lencx/opsail

⭐ 63 · Rust · Apache-2.0 · 推送 2026-08-21 · [GitHub](https://github.com/lencx/opsail) · 个人维护 · 中文 README

**给软件 agent 用的 Rust 原生工具集：网页读取与 Codex 界面改造**

以单一 CLI（opsail）为入口的模块化原生工具包，Rust crate 分别负责内容获取、Chrome 浏览器生命周期与 CDP 传输、内容提取和针对 Codex 应用的改造；另提供 Node.js 包嵌入同一原生运行时。opsail read 将静态 HTML 或浏览器渲染 DOM 转为 Markdown/HTML/JSON；opsail refit codex 在 macOS 签名应用与 Windows Store 应用上以可逆方式为 Codex 侧栏添加本地化用量信息，不做模型调用、不改应用包；Linux 不受支持。命令输出结构化 JSON、资源受限、失败静默，面向自动化场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- opsail read 将 HTML/渲染 DOM 转为 Markdown、净化 HTML 或版本化 JSON
- 接受 URL/文件/stdin/自有 Chrome 进程/借用 CDP 端点作为输入
- Codex refit 目标校验、幂等、可移除，不修改应用包
- 命令输出稳定契约、结构化诊断与机器可读 JSON

## 适用场景

- 为 agent 提供可靠、可组合的原生工具调用
- 把网页内容提取为 Markdown 供下游处理
- 在 Codex 桌面端侧栏显示本地化剩余用量信息

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L11: Opsail is a modular native toolkit that gives software agents small, composable, and reliable capabilities through 
> L17: - **Agent-ready contracts.** Commands expose stable output, structured diagnostics, bounded resource use, and quiet

## 星数曲线

```mermaid
xychart-beta
    title "lencx/opsail 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-24 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ba828c564e3a` · [字段定义](../../DATASET.md)*
