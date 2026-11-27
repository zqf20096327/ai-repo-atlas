# shi1-0yi/memsea-coopanion

⭐ 4 · JavaScript · MIT · 推送 2026-10-31 · [GitHub](https://github.com/shi1-0yi/memsea-coopanion) · 个人维护 · 中文 README

**给 Coopanion companion 的记忆做三维星海可视化与只读回捞工具**

本仓库把 memory-sea（一个可旋转的三维记忆星海可视化）接入 Coopanion：只读读取其部署目录下的消息、事实库、日记、月志等数据，按重要度×时间衰减渲染成会淡忘、被再次提及又回亮的星海；并附一个 Cortico World 扩展，为 bot 提供 memsea_recall 检索工具，上下文清空后仍能按字面相似（中文 bigram+关键词）查回旧记忆。检索非语义匹配，只看默认 30 天。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1450+ 条记忆按时间排成三维星海，颜色为类型、大小为强度
- 遗忘机制：重要度×时间衰减，复述会延长半衰期（间隔效应）
- memsea_recall 只读检索工具，不写入 bot 记忆
- 支持按 QQ 号过滤与群级 skip/fade 策略

## 适用场景

- 把 Coopanion 陪伴 bot 的长期记忆可视化浏览
- 上下文被清空后帮 bot 回捞说过的事实
- 按群配置记忆的遗忘与收录策略

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: 把 memory-sea（一片可以转的三维记忆星海）接到 Coopanion 上：**只读**它的部署目录，把她说过的话、写过的日记、记下的事实，画成一片会淡、会忘、被提起又会亮的星海；再给她一个检索工具，上下文清空之后还能把旧事捞
> L18: - **能回捞**：给 bot 一个 `memsea_recall` 工具。上下文被清掉之后，她仍然能查到"10-26 那天你说过什么"。
> L59: `extension/cortico-world-memsea/` 是一个 Cortico World 扩展：装进 Coopanion 后，她多一个 `memsea_recall` 工具，还带一段环境提示词教她什么时候该查。安装步

## 星数曲线

```mermaid
xychart-beta
    title "shi1-0yi/memsea-coopanion 星数(近 3 点)"
    x-axis ["2026-11-15", "2026-11-21", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-15 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `8bd860d05e00` · [字段定义](../../DATASET.md)*
