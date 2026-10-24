# QuentinWach/image-ranker

⭐ 93 · Python · MIT · 推送 2026-03-31 · [GitHub](https://github.com/QuentinWach/image-ranker) · 个人维护

**浏览器内两两对比并用 TrueSkill 排序图片、生成偏好数据集的 Web 工具**

Flask Web 应用：用户在浏览器中对本地目录图片做两两比较，后端用 TrueSkill 算法（μ/σ 贝叶斯技能评分）在每次比较后全局更新所有图片排名，并支持顺序淘汰（O(N) 时间）、智能洗牌与自动洗牌等加速策略。面向需要构建人类偏好数据集（如 RLHF 奖励模型训练）或整理图片集的开发者与研究者。支持本地目录直接选择、CSV 导出与断点续排、排除原因分类和图片上下文展示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TrueSkill 全局排名更新，含不确定性建模，可在不完全对比数据下排序
- 顺序淘汰可将 N 张图排名降至 O(N) 次比较
- 智能/自动洗牌优先比较高不确定性的图片
- 排名数据 CSV 导出、断点续排与自定义排除原因

## 适用场景

- 为 RLHF 奖励模型构建人类图片偏好数据集
- 从本地图片集中通过两两比较挑选更好的图片
- 对模型生成的图片做人工偏好排序以指导后训练

## 场景标签

 · 领域:数据集构建/图像标注

## 证据(README 行号)

> L24: - **TrueSkill ELO algorithm.** An advanced algorithm that takes into account the uncertainty in the ratings and upd
> L152: Post-training foundation models is what makes them actually useful. For example, large language models may not eve

## 星数曲线

```mermaid
xychart-beta
    title "QuentinWach/image-ranker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-24 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `3b4763652465` · [字段定义](../../DATASET.md)*
