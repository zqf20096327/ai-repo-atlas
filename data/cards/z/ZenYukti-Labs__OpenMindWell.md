# ZenYukti-Labs/OpenMindWell

⭐ 50 · TypeScript · NOASSERTION · 推送 2026-02-17 · [GitHub](https://github.com/ZenYukti-Labs/OpenMindWell) · 组织维护

**自托管的心理健康支持平台：匿名聊天、AI 危机检测与习惯追踪**

由 Team ZenYukti 构建的自托管开源心理健康支持平台，设计为用户用自有基础设施部署，无中心托管实例。功能包括匿名群聊室、基于 HuggingFace Inference API 情绪检测的 AI 危机检测、私密日记、习惯追踪、资源库与志愿者审核。技术栈为 React/Vite 前端加 Express/WebSocket 后端，数据存储用 Supabase，README 明确声明不能替代专业心理治疗或危机干预服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 危机检测：分析聊天消息并自动给出资源建议
- 匿名/假名账户与行级安全（Row-level security）
- 全栈自托管，宣称可全部使用免费服务部署
- 内置美/印及国际危机热线资源列表

## 适用场景

- 社区或组织自建匿名同伴支持聊天平台
- 在聊天中自动检测风险信息并提示求助资源
- 个人记录心情日记与追踪日常习惯

## 场景标签

 · 领域:健康/社区支持平台

## 证据(README 行号)

> L19: - **AI Crisis Detection** - Automatic detection of concerning messages with resource suggestions
> L70: - **Backend → HuggingFace**: Analyze chat messages for crisis detection

## 星数曲线

```mermaid
xychart-beta
    title "ZenYukti-Labs/OpenMindWell 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-29 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0e6658a33bef` · [字段定义](../../DATASET.md)*
