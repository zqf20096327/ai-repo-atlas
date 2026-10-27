# researchradar/research-radar

⭐ 37 · Python · MIT · 推送 2026-08-21 · [GitHub](https://github.com/researchradar/research-radar) · 组织维护

**自托管科研情报系统：追踪学者/主题/来源并生成可检索研究流**

面向关注快速演进技术领域者的本地优先研究情报工具：以 YAML 工作区配置关注的研究者、主题与来源，从 arXiv 与 RSS/Atom 采集内容，做规范化、去重与确定性排序（人物匹配、主题匹配、时效、来源优先级、反馈条目等），生成本地静态站点提供 Today、Reading、Search、Archive、Following 五个页面。基础循环无需 API key，LLM 与 agent（Codex/ChatGPT/Claude）为可选增强层。当前为 v0.1 alpha，学习型兴趣模型尚未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- arXiv 与 RSS/Atom 采集，规范化与规范化身份去重
- 确定性排序器，排序卡片附评分明细（Why this ranked）
- 五个本地静态页面：Today/Reading/Search/Archive/Following
- 本地优先：无 API key 可运行，LLM/agent 为可选层
- RSS 源 URL 安全检查（私网/环回/保留地址过滤、限次重定向）

## 适用场景

- 跟踪特定研究者与主题的新论文和动态
- 构建长期可检索的个人科研资料库
- 在本地聚合多个 RSS 来源并按个人优先级排序浏览

## 场景标签

`科研工具` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L141: The current baseline ranker uses transparent signals including followed-person matches, optional institution/quest
> L171: Agents enhance Research Radar; they are not required to use it.

## 星数曲线

```mermaid
xychart-beta
    title "researchradar/research-radar 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `66b38091cbdc` · [字段定义](../../DATASET.md)*
