# pumu21600-boop/Pawch-Agent

⭐ 4 · Rust · MIT · 推送 2026-11-16 · [GitHub](https://github.com/pumu21600-boop/Pawch-Agent) · 个人维护 · 中文 README

**Windows 本机桌面 AI Agent：自定义模型接入、数据本地留存**

基于 Rust（axum）服务、Svelte 前端与 Tauri 桌面壳的 Windows 本地桌面 Agent。会话、记忆、日志、用量台账全部落本机，模型走用户自有渠道，Key 经 DPAPI 加密。核心机制包括工具并行与写冲突串行、上下文整卷压缩、2D 星图记忆库、原生格式文档读写、子代理并行与定时任务、网关单点记账与花费上限、三级审批档位与执行沙箱。支持安装包与源码构建两种方式，需 Windows 10/11。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 WebView2 浏览器，agent 工具与面板操作同一实例
- 记忆库 2D 星图：向量落图、语义与词法混合排序
- Skill / MCP（三种 transport + OAuth）/ 插件沙箱四种扩展方式
- 网关单点记账：token 三路分账、花费上限到线拒绝新请求

## 适用场景

- 在本机跑一个数据不出本地的桌面 Agent 处理日常任务
- 接入自有 DeepSeek/Ollama 等渠道并管理 token 花费
- 通过 MCP 与插件扩展 agent 的工具与面板
- 用无头模式在脚本中程序化调用 agent 执行任务

## 场景标签

`AI 助手` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: **一个运行在 Windows 本机的桌面级 AI Agent —— 自定义模型接入，数据本地留存，任务闭环执行**
> L18: **Pawch Agent 是一个装在 Windows 本机的桌面级 Agent**：Rust（axum）服务 + Svelte 前端 + Tauri 桌面壳。会话、记忆、日志、用量台账全落本机；模型接你自己的渠道，Key 经 D

## 星数曲线

```mermaid
xychart-beta
    title "pumu21600-boop/Pawch-Agent 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-21"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-08 4 → 2026-11-21 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e203da9a2cd7` · [字段定义](../../DATASET.md)*
