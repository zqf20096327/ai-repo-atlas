# longlivewama/CourtVision-AI

⭐ 3 · Python · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/longlivewama/CourtVision-AI) · 个人维护

**网球比赛视频计算机视觉分析工具：检测、追踪与战术统计**

将网球计算机视觉 notebook 整理为可复用 Python 包，并提供三种调用同一 pipeline 的接口：React+FastAPI 网页应用、Streamlit 应用与 tennis-cv CLI。上传广播视角视频后执行球体检测（自定义 YOLOv8x）、零样本球员检测（Grounding-DINO-tiny）、DeepSORT 追踪、实例分割、轨迹、热图、弹跳与回合候选、球速估计；在提供参考标定时可生成俯视球场视图与 JSON 分析摘要。README 明确标注各输出的局限：不做姿态估计、不推断比分、标定与相机绑定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种分析模式共用同一 tennis_cv pipeline（球检测/球员检测/追踪/全分析/高级分析）
- Grounding-DINO-tiny 零样本球员检测 + DeepSORT 追踪，无需球员专属训练
- 双阶段 analytics 流水线输出标注视频与 JSON 摘要（回合、弹跳、速度、耗时）
- 参考单应性标定下的俯视球场面板，无标定时明确提示不可用

## 适用场景

- 上传网球比赛视频生成带标注的分析视频
- 查看球员移动热图、回合分割与弹跳候选等时间维统计
- 用 CLI 批量跑单一检测或追踪任务

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: **Tennis match video analysis with object detection, multi-object tracking, instance segmentation, temporal analytic
> L5: CourtVision AI takes a broadcast-style tennis clip and renders an annotated output video: ball detection, zero-shot 
> L16: - Detect and follow the ball and the two players in a singles match video.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `43b1a965b51d` · [字段定义](../../DATASET.md)*
