# murtiunlimited/face-emotion-recognition

⭐ 55 · Python · MIT · 推送 2026-05-18 · [GitHub](https://github.com/murtiunlimited/face-emotion-recognition) · 个人维护

**CNN 实时人脸表情识别系统：桌面摄像头与浏览器双形态**

基于轻量 CNN 的人脸表情检测项目：输入 48×48 灰度人脸图像，识别 Angry/Disgust/Fear/Happy/Sad/Surprise/Neutral 七类表情。提供两条运行路径——OpenCV 桌面摄像头推理，以及 FastAPI 后端加浏览器前端（调用摄像头）的 Web 版本，另附 shell 脚本一键跑通预处理、训练与启动全流程。使用方式为本地创建虚拟环境并 pip 安装依赖后，运行数据预处理、模型训练和推理脚本；模型文件需存在于 model_artifacts 目录。项目描述称接入 GroqCloud 用于聊天功能，README 可见部分未展开。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 轻量 CNN 识别 7 类表情（48×48 灰度输入）
- OpenCV 桌面摄像头与 FastAPI+浏览器两种推理形态
- shellscript.sh 一键执行预处理+训练+启动全流程

## 适用场景

- 用笔记本摄像头实时检测人脸表情
- 在浏览器中体验表情识别 Web 应用
- 学习 CNN 训练与 FastAPI 部署的完整流程

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: This project performs **real-time facial emotion detection** using a CNN model.
> L95: - Architecture: Lightweight CNN

## 星数曲线

```mermaid
xychart-beta
    title "murtiunlimited/face-emotion-recognition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-26 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f342427ccc61` · [字段定义](../../DATASET.md)*
