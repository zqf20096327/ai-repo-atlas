# shure-dev/small-vlm-sop-check

⭐ 54 · Python · MIT · 推送 2026-08-11 · [GitHub](https://github.com/shure-dev/small-vlm-sop-check) · 个人维护

**面向工厂一人称视频的小型 VLM 时间定位训练评估平台**

以 Temporal Grounding 为核心的开发基盘：对工厂一人称短视频做人手日文事件标注，用统一 JSON 契约对 ≤4B 的候选 VLM（Marlin-2B、Qwen3.5、Qwen3-VL、Gemma 等，经 4bit MLX 转换）进行区间预测对比，以 tIoU 评估；提供 Web 标注/结果比对应用（sop-app/sop-view）、CLI 评估与数据集管理，可用 sop-export-ms-swift 输出 ms-swift 后端的 LoRA/QLoRA 训练数据。目标场景为 Connected Worker 手顺检查，但 README 声明为 experimental，尚未验证实时推理、可穿戴设备部署与告警逻辑，且不用于自动安全判断。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 人手日文事件标注 + 模型预测区间的 tIoU 对比评估流水线
- 多个 ≤4B VLM（MLX 4bit）在同一数据契约下的基准矩阵
- sop-app Web 标注工作区（时间线拖拽调整、tIoU 即时重算）
- sop-export-ms-swift 输出 ms-swift 后端 LoRA/QLoRA 训练数据

## 适用场景

- 为工厂一人称视频构建事件时间区间的正解标注集
- 在统一评测口径下比较多个小型 VLM 的时间定位能力
- 把标注数据导出为 ms-swift 训练集做微调并复评
- 用只读模式向团队展示模型评估结果

## 场景标签

`模型评测` `微调` · 领域:评测与运维

## 证据(README 行号)

> L27: そのための基礎能力として、このリポジトリは動画内のイベント区間を特定する**Temporal Grounding**を中心に扱います。
> L119: sop-check eval \
> L137: 完成したデータは `sop-export-ms-swift` で動画SFT JSONLへ出力し、ms-swiftをbackendとしてLoRA/QLoRAを準備できます。学習前後は同じ契約とsplitで比較します。

## 星数曲线

```mermaid
xychart-beta
    title "shure-dev/small-vlm-sop-check 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-27 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d33a98bd2ef3` · [字段定义](../../DATASET.md)*
