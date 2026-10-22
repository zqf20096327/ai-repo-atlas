# xgzlucario/githubhunt

⭐ 156 · Python · MIT · 推送 2025-12-25 · [GitHub](https://github.com/xgzlucario/githubhunt) · 个人维护 · 中文 README

**AI Agent 驱动的自然语言 GitHub 仓库搜索工具**

用户用自然语言描述需求，AI Agent（DeepSeek API）识别意图，调用内置搜索工具迭代调整查询，结合本地 MeiliSearch 索引（frequency 匹配策略）实现 GitHub 仓库检索。还支持视觉理解模型分析仓库流程图（需 Steel Browser 与 QWEN API）、从用户 starred 列表搜索、总结仓库功能。需先通过 fetch_repos.py 同步仓库构建索引，用 uv 管理依赖，系统依赖含 MeiliSearch、Python 3.13、DeepSeek API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言驱动的 Agent 迭代式仓库搜索
- 本地 MeiliSearch 索引（frequency 匹配策略）提升召回率
- 视觉理解模型分析仓库流程图（Steel Browser + QWEN）
- 支持从用户 starred 列表中搜索

## 适用场景

- 用一句话描述需求精准查找 GitHub 仓库
- 让 AI 解释某个仓库的流程图或功能
- 在自己关注的仓库列表里做语义搜索

## 场景标签

 · 领域:开发者工具/代码搜索

## 证据(README 行号)

> L3: githubhunt 是一个基于 AI Agent 的自然语言 Github 仓库搜索工具, 用户通过使用自然语言描述需求, 例如: "查找 golang 实现的 redis 服务器, 基于 AELoop", AI Agent 会识
> L13: - 使用视觉理解模型分析仓库, 例如: "解释 xgzlucario/rotom 的流程图"

## 星数曲线

```mermaid
xychart-beta
    title "xgzlucario/githubhunt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 155 --> 157
    line [156, 156]
```

2026-10-18 156 → 2026-10-22 156（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1d7f0bb0f84d` · [字段定义](../../DATASET.md)*
