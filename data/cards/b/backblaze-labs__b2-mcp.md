# backblaze-labs/b2-mcp

⭐ 46 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/backblaze-labs/b2-mcp) · [官网](https://backblaze-labs.github.io/b2-mcp/) · 组织维护

**Backblaze 官方 B2 云存储 MCP 服务器，供 AI 客户端操作存储**

Backblaze Labs 维护的 Model Context Protocol 服务器，让 Claude 等 MCP 兼容 AI 客户端通过 40 个工具操作 B2 云存储：17 个 B2 原生 SDK 控制面工具、19 个 S3 兼容数据面工具（上传/下载/生命周期/预签名 URL）及 4 个自定义分析工具。机制上：破坏性操作默认需确认，密钥默认不进入模型上下文，工具注册按密钥能力裁剪。支持 npx、Claude Desktop 扩展包、Docker（HTTP/stdio）部署，附 Markdown 技能包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40 个工具覆盖 B2 控制面、S3 数据面与分析
- 破坏性操作门控与密钥脱离模型上下文的 secret sink 机制
- 按密钥能力裁剪工具注册（非主密钥显示 37 个）
- npx / Claude Desktop 扩展 / Docker 多途径部署

## 适用场景

- 在 Claude 等 AI 客户端中直接管理 B2 桶、文件与密钥
- 通过对话完成对象上传下载与预签名链接生成
- 查看存储增长、流量与大文件等 B2 报表分析

## 场景标签

 · 领域:云存储/AI 工具接入

## 证据(README 行号)

> L22: A Model Context Protocol server for Backblaze B2 Cloud Storage. It lets any MCP-compatible AI client (Claude, and o
> L28: - **Native B2 SDK (`@backblaze-labs/b2-sdk`) (17)** — B2 control-plane operations the S3 API has no equivalent for:

## 星数曲线

```mermaid
xychart-beta
    title "backblaze-labs/b2-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-29 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b2af37676dd1` · [字段定义](../../DATASET.md)*
