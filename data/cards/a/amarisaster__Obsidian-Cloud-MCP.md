# amarisaster/Obsidian-Cloud-MCP

⭐ 10 · TypeScript · Apache-2.0 · 推送 2026-08-11 · [GitHub](https://github.com/amarisaster/Obsidian-Cloud-MCP) · 个人维护

**让 Claude 通过 MCP 远程读写 Obsidian 笔记库的工具**

由 Obsidian 插件与 Cloudflare Worker 两部分组成：插件监视笔记变更并同步到 Cloudflare R2（含自动/全量/选择性同步与哈希比对），Worker 将 vault 暴露为 MCP 端点（SSE 与 Streamable HTTP 两种传输），并提供搜索索引重建 API。用户在 Claude Web/Desktop/Phone 或 Claude Code 中配置连接后，可通过 4 个工具读写、搜索、管理笔记文件与元数据。部署依赖 Cloudflare 账号与 Node.js，免费套餐含 10 GB 存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 插件监视文件变更，2 秒防抖推送至 R2，支持哈希比对增量同步
- Worker 将 vault 暴露为 MCP 端点，支持 SSE 与 Streamable HTTP 传输
- 提供 vault_file/vault_browse/vault_meta/vault_sync 四个 MCP 工具
- 后台批量构建搜索索引（每批 50 个文件）

## 适用场景

- 在手机或网页端让 Claude 读取和检索我的 Obsidian 笔记
- 通过对话让 Claude 代我写入或整理笔记文件
- 多设备访问同一份云同步的笔记库

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5: An Obsidian plugin syncs your vault to Cloudflare R2. A Cloudflare Worker exposes it as an MCP endpoint. Claude read
> L69: ### 5. Connect Claude
> L88: |Tool|Actions|Description|

## 星数曲线

```mermaid
xychart-beta
    title "amarisaster/Obsidian-Cloud-MCP 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `e077db9f35ae` · [字段定义](../../DATASET.md)*
