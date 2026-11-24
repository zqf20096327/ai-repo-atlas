# vipulawl/reddit-leads

⭐ 3 · Python · AGPL-3.0 · 推送 2026-11-05 · [GitHub](https://github.com/vipulawl/reddit-leads) · 个人维护

**自托管 Reddit 销售线索发现工具：LLM 区分真实买家**

粘贴网站 URL 后，工具读取首页与定价页生成产品画像，再轮询订阅的 subreddit 与全站关键词搜索，经三阶段漏斗（关键词匹配→本地 bge-small 嵌入过滤→LLM 意图判定）筛选出真实求购帖，排除自我推广，输出带标签与 0–100 匹配分的线索看板。支持 Reddit 官方 API 或无密钥的公共 RSS 两种读取方式，单用户自托管无账号体系，AGPL v3 许可，Docker 或 Python/Node 源码两种运行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三阶段筛选漏斗：关键词匹配、本地嵌入过滤、LLM 意图打分
- 支持 Reddit API（每 60 秒）或公共 RSS（约 5 分钟）两种读取方式
- 线索卡片支持人工纠正标签，纠正样本进入后续打分提示词
- 可全程零成本配置：RSS + 本地 Ollama 模型

## 适用场景

- 为独立开发者的产品在 Reddit 上寻找潜在客户帖子
- 自托管监控多个 subreddit 的求购与工具推荐讨论
- 无 Reddit API 密钥时用 RSS 做轻度个人使用

## 场景标签

 · 领域:市场营销/线索发现

## 证据(README 行号)

> L5: An open-source, self-hosted Reddit lead generation and social listening tool. It watches subreddits and keyword sear
> L18: |3. Intent|matches are grouped by thread (a matching comment pulls in its parent post), and each thread is judged o


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `c93f3cb1f93b` · [字段定义](../../DATASET.md)*
