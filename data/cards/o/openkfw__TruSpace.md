# openkfw/TruSpace

⭐ 25 · TypeScript · GPL-3.0 · 推送 2026-10-18 · [GitHub](https://github.com/openkfw/TruSpace) · [官网](https://web.truspace.dev) · 组织维护

**去中心化的主权文档协作工作区，内置本地 AI 解读**

面向不愿将数据交给云服务商的组织间文档协作平台：每个组织运行自己的节点，文档、版本与元数据通过 IPFS/IPFS Cluster 点对点同步，IPFS Cluster 编排 pin 保障可用性，敏感数据与文档加密存储于本地 SQLite 与工作区。AI 为辅助能力：通过 Ollama 与 Open Web UI 容器在本地运行 LLM，用可定制提示解读文档，不向外部 API 发送内容。以 Docker 容器编排部署，TypeScript/React/Next.js 构建，GPL v3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 IPFS/IPFS Cluster 的点对点文档同步与自动复制
- 本地 LLM（Ollama + Open Web UI）解读文档，无外部 API 调用
- 无中央服务器，可运行私有 IPFS 网络，跨节点通信加密
- Docker 容器化部署，git clone 后 start.sh 一键启动

## 适用场景

- 与监管方、子公司等不完全受控的伙伴协作敏感文档
- 不想使用云服务商的组织搭建自托管文档协作网络
- 在自有基础设施上用本地 AI 理解共享文档内容

## 场景标签

`文档问答` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L21: It's a network where every participant (or organization) runs their **own node**. Documents, versions, and metadata
> L28: - 🧠 **AI-assisted, not AI-dependent** — local LLMs (Ollama + Open Web UI) help interpret documents with customizabl

## 星数曲线

```mermaid
xychart-beta
    title "openkfw/TruSpace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b9996d68b6d3` · [字段定义](../../DATASET.md)*
