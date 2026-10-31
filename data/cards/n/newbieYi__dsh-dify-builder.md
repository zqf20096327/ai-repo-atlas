# newbieYi/dsh-dify-builder

⭐ 16 · JavaScript · MIT · 推送 2026-09-07 · [GitHub](https://github.com/newbieYi/dsh-dify-builder) · 个人维护 · 中文 README

**在 DeepSeek Harness 中对话式构建本地 Dify 工作流的安装器与插件**

为 DeepSeek Harness（DSH）提供 Dify 工作流构建能力的安装器：通过 npx 一键下载固定版本的 Dify、启动 Docker 容器、初始化本地管理员、安装 DSH 插件/右侧画布面板与 Agent preset，并尝试同步 DeepSeek Key 配置官方模型插件。安装后用户在 DSH 左侧对话描述需求，右侧 Dify 画布实时更新节点与连线。草稿保存基于 Dify 原生 collaboration 模式与 Socket.IO。面向使用 DSH 的开发者/用户；当前支持 macOS 与 Linux，Windows 未完成端到端验证；无模型 Key 时仍可使用非模型工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- npx 一键安装：自动下载固定版本 Dify 并启动 Docker 容器、初始化本地管理员
- 对话实时生成/修改 Dify 工作流，画布原地更新不刷新页面
- 安装器逐项验收（CLI/Docker/插件冲突/协作端点），重复执行安全
- 提供只读诊断命令 doctor 检查环境问题

## 适用场景

- 在 DeepSeek Harness 中用自然语言搭建 Dify 工作流
- 本地快速部署带 Dify 画布面板的 DSH 开发环境
- 安装后排查 Dify/DSH/Docker 环境问题

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: 在 DeepSeek Harness 中通过对话实时构建本地 Dify 工作流。右侧直接显示 Dify 画布，节点和连线原地更新，不反复刷新页面。
> L73: 5. 尝试安装 Dify 官方 DeepSeek 模型插件；存在 DSH DeepSeek Key 时同步凭据并选择可用模型。

## 星数曲线

```mermaid
xychart-beta
    title "newbieYi/dsh-dify-builder 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `517a157052e3` · [字段定义](../../DATASET.md)*
