# kwistzzqq-byte/image2-ads-studio

⭐ 48 · TypeScript · Apache-2.0 · 推送 2026-05-06 · [GitHub](https://github.com/kwistzzqq-byte/image2-ads-studio) · 个人维护 · 中文 README

**面向 Image2 广告作图的开源 Prompt Agent**

把客户白话需求、文案、行业与参考图解析为结构化广告方案，再生成去品牌化、可直接投入生产的图像提示词。流程为：意图解析→模板检索（320 个业务模板、240 个视觉配方）→LLM 提示词大脑重写→确定性校验→输出优化提示词。提供本地 Web 工作台（pnpm 安装、Responses 兼容 LLM 端点），社区版不调用图像生成 API，需将提示词手动粘贴到 Image2 等工具；另有商业版提供私有模板与适配器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 320 个业务模板 + 240 个视觉配方开源模板库
- 解析客户简报并生成去品牌化生产级提示词的完整流水线
- 确定性提示词校验（构图/光影/字体/材质/参考图策略）
- 本地 Web 提示词工作台（简报输入、优化输出、检索信号）

## 适用场景

- 把本地商家白话需求转成结构化广告图提示词
- 门店招牌、海报、电商主图等广告垂类批量生成提示词
- 在 Image2 等图像生成工具中测试与复用去品牌化提示词

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: Advertising prompt agent for Image2: turn business briefs and reference images into debranded, production-ready imag
> L59: - LLM prompt brain: uses a Responses-compatible LLM endpoint to refine the rule prompt.

## 星数曲线

```mermaid
xychart-beta
    title "kwistzzqq-byte/image2-ads-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-29 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `801c15bd9e77` · [字段定义](../../DATASET.md)*
