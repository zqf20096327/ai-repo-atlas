# pogzyb/tourist

⭐ 29 · Python · MIT · 推送 2026-06-02 · [GitHub](https://github.com/pogzyb/tourist) · 个人维护

**面向 LLM 工具调用的开源自建 SERP/网页抓取服务**

由 Service（HTTP API）与 Client 组成的 SERP 提取与网页抓取应用：Service 处理搜索结果提取与无头浏览抓取请求，Client（pip 安装）供应用、agent 或抓取脚本调用以构建 LLM 工具、抓取应用或自动化测试流程。支持 Docker 本地运行、AWS 与 Azure serverless 部署，数据不经第三方处理。README 声明处于早期开发阶段，API 可能变动；serverless 部署仍有使用成本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Service/Client 双组件架构，数据不经第三方处理
- 提供 MCP 模式（Azure 部署下）
- Docker 本地运行与 AWS/Azure serverless 部署路径
- Python 客户端可构建 LLM 工具（示例搭配 LlamaIndex/Ollama）

## 适用场景

- 为 LLM agent 构建搜索与网页抓取工具替代付费 SERP API
- 自部署 SERP 服务控制数据流向
- 自动化测试或抓取脚本中调用 HTTP API

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: An open-source, low-cost, serverless application for SERP extraction and web scraping.
> L7: Work on LLM projects without worrying about credits, subscriptions, or rate-limits. Tourist is a free alternative to
> L84: Build your own LLM tools, web scraping apps, or automated testing workflows with the Tourist client.

## 星数曲线

```mermaid
xychart-beta
    title "pogzyb/tourist 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c2529c53a08d` · [字段定义](../../DATASET.md)*
