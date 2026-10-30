# opengenesishq/EastGenesis

⭐ 111 · TypeScript · AGPL-3.0 · 推送 2026-09-27 · [GitHub](https://github.com/opengenesishq/EastGenesis) · [官网](https://www.caogen.dev) · 组织维护 · 中文 README

**智能模型路由的本地 AI 助手桌面应用，自动为任务选模型**

基于 Electron 的本地优先 AI 桌面助手，核心机制是智能模型路由：识别任务类型（编码/长文本/推理等），按能力、成本、延迟、预算对候选模型多维度评分后自动选择，Provider 故障或限流时自动切换并保留上下文。支持 OpenAI、Anthropic、Azure OpenAI 及经 OpenAI 兼容接口接入的国产模型。附带 Office 文件生成（DOCX/XLSX/PPTX/PDF）、内置浏览器、文件/终端/Git 开发工具与 MCP 集成。当前为 v0.1.9-beta 社区版，macOS 可下载，Windows 构建中，Linux 暂不支持；真实 Provider 大规模验证待完善。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 任务类型识别与多维度模型自动评分路由
- Provider 故障/限流自动切换且保留上下文
- Word/Excel/PPT/PDF 文件生成
- MCP 工具集成与成本预算控制

## 适用场景

- 输入编程、文档总结等任务，让系统自动选择模型并查看路由依据
- 配置多个 Provider 实现自动切换与成本控制
- 在本地桌面完成 AI 对话、浏览与 Office 文档生成

## 场景标签

`模型网关` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L3:  智能模型路由 AI 助手
> L16: ## 🎯 核心特性：智能模型路由
> L39: ### 🌐 多 Provider 支持

## 星数曲线

```mermaid
xychart-beta
    title "opengenesishq/EastGenesis 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 110 --> 119
    line [118, 111, 111]
```

2026-10-18 118 → 2026-10-30 111（-7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `de70b81b5173` · [字段定义](../../DATASET.md)*
