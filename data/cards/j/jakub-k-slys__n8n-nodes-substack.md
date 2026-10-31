# jakub-k-slys/n8n-nodes-substack

⭐ 27 · TypeScript · MIT · 推送 2026-06-27 · [GitHub](https://github.com/jakub-k-slys/n8n-nodes-substack) · [官网](https://iam.slys.dev) · 个人维护

**n8n 的 Substack 只读集成节点：读取档案/文章/评论数据**

面向自托管 n8n 用户的社区节点包，将 Substack 接入 n8n 工作流。提供只读操作：获取作者档案与出版物数据、分页读取文章、读取文章评论，另支持笔记的读取与创建。通过 npm 安装后重启 n8n 生效，凭据配置为出版物地址与 Substack API key。README 顶部声明本包已被 n8n-nodes-substack-new 取代，不再积极开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 档案/文章/笔记/评论四类资源的读取操作
- npm 安装，配置出版物地址与 API key 即可使用
- 笔记支持创建，其余操作为只读

## 适用场景

- 在 n8n 工作流中拉取 Substack 出版物的内容与数据
- 构建 Substack 内容发现或分析类自动化流程

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L13: Read-only n8n community node for Substack. Enables content discovery and
> L27: ```bash

## 星数曲线

```mermaid
xychart-beta
    title "jakub-k-slys/n8n-nodes-substack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c819e21d5849` · [字段定义](../../DATASET.md)*
