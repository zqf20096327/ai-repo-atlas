# openai/teen-safety-policy-pack

⭐ 28 · Apache-2.0 · 推送 2026-03-24 · [GitHub](https://github.com/openai/teen-safety-policy-pack) · 组织维护

**面向青少年保护的提示词安全策略包，配合安全模型做分类**

OpenAI 发布的一组提示词形式的安全策略，初始覆盖 6 个政策领域（暴力、色情、身体意象、危险活动、角色扮演、年龄受限商品服务）。开发者从 example_policies/ 选取策略提示词，与 gpt-oss-safeguard（120b/20b，托管于 Hugging Face）配合使用，将安全要求转化为内容分类器；输出标签可映射到实时过滤、离线审核、分诊或监控流程。datasets/ 提供与策略配对的 CSV 验证集，用于提示词迭代的回归测试。README 声明策略仅为起点而非完整定义，建议按产品场景改造并与其他防护结合。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个初始青少年安全策略领域，以提示词形式提供
- 与 gpt-oss-safeguard 模型配合生成内容分类器
- datasets/ 提供与策略配对的验证集用于回归测试
- 通过 ROOST Model Community 接受开源协作贡献

## 适用场景

- 为面向青少年的产品构建实时内容过滤分类器
- 对用户生成内容做离线安全审核与分诊
- 在修改提示词前后用验证集度量性能变化

## 场景标签

 · 领域:AI 安全/内容审核

## 证据(README 行号)

> L10: The Teen Safety Policy Pack is a set of prompt-based safety policies designed to create age-appropriate protections
> L12: These policies are structured as prompts that can be directly used with `gpt-oss-safeguard`, enabling developers to
> L41: Policy validation datasets live in `datasets/` as policy-specific CSV files. The filenames mirror the policy slugs 

## 星数曲线

```mermaid
xychart-beta
    title "openai/teen-safety-policy-pack 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-26 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5e413786d99a` · [字段定义](../../DATASET.md)*
