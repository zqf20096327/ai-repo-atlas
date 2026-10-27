# harivilasp/Interview-Video-Analysis

⭐ 58 · JavaScript · 推送 2026-05-10 · [GitHub](https://github.com/harivilasp/Interview-Video-Analysis) · 个人维护

**开源视频面试评估平台：情绪检测、语音分析与简历匹配打分**

面向招聘公司与求职者的视频面试分析平台。系统从录制的面试视频中提取三类信号：Keras CNN（FER-2013 训练）对 OpenCV 人脸帧做逐帧情绪分类；Parselmouth 封装 Praat 测量语速、停顿、填充词与音高变化；NLTK + TF-IDF 余弦相似度计算简历与职位描述的匹配分。后端为 Flask + MongoDB，前端为 React + WebRTC，公司可发布职位、安排面试并查看分析结果，求职者可练习面试并上传简历。需自行部署前后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- FER-2013 训练的 Keras CNN 逐帧情绪分类
- 基于 Praat/Parselmouth 的语速、停顿、填充词等语音指标
- TF-IDF 余弦相似度的简历-职位描述匹配评分
- React + WebRTC 浏览器内视频面试与 Flask/MongoDB 后端

## 适用场景

- 招聘方对录制面试做多维度自动评估并查看情绪时间线
- 求职者练习面试并根据语音与情绪反馈改进表现
- 公司筛选时核验候选人与职位描述的文本匹配度

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L8: An open-source platform that automates video interview evaluation using computer vision, speech analysis, and NLP. D
> L18: |**Facial emotions**|Keras CNN on FER-2013|Frame-by-frame emotion distribution (happy, sad, angry, neutral, surpris

## 星数曲线

```mermaid
xychart-beta
    title "harivilasp/Interview-Video-Analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-27 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ec2451b73017` · [字段定义](../../DATASET.md)*
