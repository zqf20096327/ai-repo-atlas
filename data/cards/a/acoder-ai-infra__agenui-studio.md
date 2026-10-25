# acoder-ai-infra/agenui-studio

⭐ 79 · Go · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/acoder-ai-infra/agenui-studio) · 组织维护 · 中文 README

**自托管工作台：用 AI agent 生成可执行的数据绑定界面**

自托管的 AGenUI 界面构建与运行环境：配置 OpenAI 兼容或 Anthropic Messages API 的模型端点后，通过规则驱动的 agent 生成卡片界面，支持实时预览、受保护的多轮编辑，输出可脱离 Studio 运行的 Runtime Package（含数据源、绑定、操作符）。内置 SQLite 知识库、BM25 检索、Markdown 规则与 Web 渲染器，存储/热状态/知识源等端口可替换为 MySQL、Redis、MCP 服务。需 Go 1.26.2+ 与 Node.js 20+ 从源码运行，面向接入自有模型 API 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 契约优先的意图到可执行 UI 生成路径与受保护多轮编辑
- Runtime Package 可脱离 Studio 连接独立执行数据绑定与操作符
- 本地默认自包含（SQLite/BM25/Markdown 规则/内置渲染器），各端口可替换
- 支持 OpenAI 兼容与 Anthropic Messages API 接入用户自有模型

## 适用场景

- 用自有模型生成带数据绑定和操作符的卡片界面
- 将生成的 Runtime Package 发布并嵌入生产应用
- 在自托管控制台管理知识、API 定义、操作符与设计规则

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L7: AGenUI Studio is a self-hosted workspace for building, running, and iterating on
> L67: - Configure your own OpenAI-compatible or Anthropic Messages API endpoint and

## 星数曲线

```mermaid
xychart-beta
    title "acoder-ai-infra/agenui-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-25 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `648e95f34a54` · [字段定义](../../DATASET.md)*
