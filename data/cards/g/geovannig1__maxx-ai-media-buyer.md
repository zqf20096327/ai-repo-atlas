# geovannig1/maxx-ai-media-buyer

⭐ 3 · TypeScript · Apache-2.0 · 推送 2026-11-17 · [GitHub](https://github.com/geovannig1/maxx-ai-media-buyer) · 个人维护

**面向 Meta 广告投放者的自托管 AI 广告代理应用**

自托管的开源广告投放管理应用：从一句话简报起草完整 Meta 广告系列、生成并打分文案、每日审计账户找出浪费花费、将建议转为待审批的变更卡片。所有数字来自对同步广告数据与业务成交记录的确定性代码计算，并标注来源与置信度；广告系列默认以暂停状态创建，所有写入需人工批准，AI 为可选项（AI_PROVIDER=none 时报告与打分仍可用）。技术栈为 Next.js + TypeScript，内置 46 个只读工具的 MCP server。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从一句话简报起草 Meta 广告系列，创建后为暂停状态并读回验证
- 文案生成加确定性规则打分（长度、钩子、政策风险、重复等）
- 归因对齐业务实际记录的订单/线索/预约，与 Meta 建模结果并排呈现
- MCP server 提供 46 个只读工具，可接入 Claude Desktop 等 MCP 客户端

## 适用场景

- 用一句话简报起草并审批完整的 Meta 广告系列
- 审计广告账户找出浪费的花费与效果下降原因
- 按品牌语气批量生成并打分广告文案
- 将广告效果与业务实际成交记录做归因核对

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L28: Maxx is a self-hosted AI ad agency for **Meta ads** and the answer to your ad questions: it drafts
> L113: - **AI optional.** One gateway over Claude (Anthropic API, Bedrock, Vertex, Foundry) and any

## 星数曲线

```mermaid
xychart-beta
    title "geovannig1/maxx-ai-media-buyer 星数(近 2 点)"
    x-axis ["2026-11-27", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-27 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `1e8152e0eb1e` · [字段定义](../../DATASET.md)*
