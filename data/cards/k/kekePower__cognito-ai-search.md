# kekePower/cognito-ai-search

⭐ 283 · TypeScript · MIT · 推送 2026-05-11 · [GitHub](https://github.com/kekePower/cognito-ai-search) · [官网](https://blog.kekepower.com/blog/2025/may/30/new_release_-_cognito_ai_search_120.html) · 个人维护

**本地 AI 助手与隐私网页搜索结合的自托管搜索页**

基于本地 LLM（经 Ollama 接入 LLaMA/Mistral 等模型）与自托管 SearXNG 元搜索引擎的私有搜索与问答 Web 应用，全部运行在用户自己的硬件上。对话不出本机，搜索不记录、不建画像；支持 IPv6 配置、双主题界面、PDF 导出与缓存机制。以 Docker 预构建镜像（Docker Hub 提供 latest/1.2.0/1.1.0 标签）方式部署，通过环境变量配置 Ollama 与 SearXNG 地址及默认模型，MIT 许可。面向重视隐私的个人用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 经 Ollama 接入本地模型，对话不离开本机
- 使用自托管 SearXNG 实现无追踪的聚合网页搜索
- 提供 Docker Hub 预构建镜像与环境变量配置
- 支持 IPv6 访问与亮/暗双主题

## 适用场景

- 在本机或自有服务器上搭建隐私优先的 AI 问答与搜索页面
- 无追踪地聚合搜索多个搜索引擎的结果
- 离线环境下使用本地模型获得回答

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: Cognito AI Search offers a secure and private way to find information and get answers. It's designed for individuals
> L26: Imagine having an AI assistant that operates entirely on your own computer. Cognito AI Search makes this possible b
> L34: When you need to search the wider internet, Cognito AI Search uses a self-hosted instance of SearXNG. This is a pow

## 星数曲线

```mermaid
xychart-beta
    title "kekePower/cognito-ai-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 282 --> 284
    line [283, 283]
```

2026-10-18 283 → 2026-10-27 283（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a91c19af97f0` · [字段定义](../../DATASET.md)*
