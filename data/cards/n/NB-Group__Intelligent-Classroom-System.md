# NB-Group/Intelligent-Classroom-System

⭐ 20 · Python · GPL-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/NB-Group/Intelligent-Classroom-System) · 个人维护 · 中文 README

**课堂学生行为检测系统：YOLOv8+CNN 识别听课/走神等行为**

基于计算机视觉的课堂学生行为检测系统：用 YOLOv8 分割画面中的学生个体，输入作者自建的 CNN 模型分类行为（听课、喝水、走神、写字），训练集由作者自行采集标注，README 声明准确率 99.86%，并以 face_recognition 做人脸识别对应学生身份。需注册 Ultralytics 账号填写 API key，可实时摄像头或视频检测，CPU 可运行。作者在 README 顶部声明该项目为其少年时期所作，不推荐用于真实环境，并称其具有隐私侵犯性；GPL v3 许可且禁止商用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | GPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- YOLOv8 分割 + 自建 CNN 分类四种学生行为
- face_recognition 用于学生身份识别
- 支持实时摄像头与已有视频两种检测方式
- 无需额外配置，CPU 可运行

## 适用场景

- 课堂中检测学生听课/走神等行为并统计注意力分布
- 对已有课堂录像进行行为识别分析

## 场景标签

`人脸识别` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L13: It is a project that utilizes artificial intelligence computer vision technology to detect student behavior in the 
> L20: This project uses YOLOV8 for image segmentation, separating each student in the classroom scene. The segmented imag

## 星数曲线

```mermaid
xychart-beta
    title "NB-Group/Intelligent-Classroom-System 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-31 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5eff32b601f8` · [字段定义](../../DATASET.md)*
