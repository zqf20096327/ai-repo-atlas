# GoogleCloudPlatform/cymbal-air-toolbox-demo

⭐ 350 · Python · Apache-2.0 · 推送 2026-08-14 · [GitHub](https://github.com/GoogleCloudPlatform/cymbal-air-toolbox-demo) · [官网](https://github.com/googleapis/genai-toolbox/) · 组织维护

**虚构航空公司客服 Agent 示例：LangGraph+RAG 经 MCP Toolbox 访问数据库**

GoogleCloudPlatform 发布的演示项目（非官方支持产品），以虚构航空公司 Cymbal Air 为例，展示如何构建使用 Agent 与 RAG 查询、操作云端数据库的应用。架构含三部分：面向用户的 agentic 应用、将数据库操作暴露为工具集的 MCP Toolbox 中间件服务器、以及可替换的数据库。部署流程为克隆仓库、下载 Toolbox 二进制、一次性数据库与 tools.yaml 配置，Toolbox 可本地运行或部署到 Cloud Run。面向希望在 Google Cloud 上构建 Agentic 应用的开发者，可作为自定义工具的起点。

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

- Agent 编排：LLM 自主决定工具调用顺序（如 find_flights、list_amenities）
- MCP Toolbox 中间件将数据库操作暴露为工具集，代理不直接访问数据库
- 数据库设计为可替换，便于运行在偏好的数据库上
- RAG 增强回答，降低幻觉

## 适用场景

- 参考实现构建连接云端数据库的客服 Agent
- 学习 MCP Toolbox 工具配置与 Agent 编排模式
- 以该 demo 为起点自定义 Agent 工具集

## 场景标签

`Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L14: This project provides a production-quality reference implementation for building
> L18: This demonstration features Cymbal Air, a fictional airline. The application
> L19: showcases a customer service assistant that helps travelers manage flights and

## 星数曲线

```mermaid
xychart-beta
    title "GoogleCloudPlatform/cymbal-air-toolbox-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 349 --> 351
    line [350, 350]
```

2026-10-18 350 → 2026-10-30 350（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `aa29957881e0` · [字段定义](../../DATASET.md)*
