# NoahOksuz/DentalXrayAI

⭐ 50 · HTML · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/NoahOksuz/DentalXrayAI) · [官网](https://xray.cyphersec.eu/) · 个人维护

**牙科全景 X 光目标检测的 WebUI 与模型**

基于全景牙科数据集（CC BY 4.0）训练的 YOLO26 目标检测项目，附带 Web 界面提交查询。模型检测 6 个类别：修复体、根管、龋齿、阻生、修复材料与残根。仓库根目录附带训练好的 best.pt 权重，可通过 pip 安装依赖后本地运行；README 同时给出训练与评估流程（Roboflow 下载、ultralytics 训练、yolo val 测试集评估），并注明龋齿是最弱类别，项目为研究/演示用途、非医疗器械、不可用于诊断。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLO26m 检测模型（best.pt）随仓库分发，检测 6 个牙科类别
- 提供 Web 界面查询模型，本地运行于 http://127.0.0.1:8080
- README 给出完整训练与测试集评估命令（含指标输出）
- 声明龋齿检测最弱，非医疗设备、不可用于诊断

## 适用场景

- 本地部署牙科全景片目标检测演示界面
- 用公开全景牙科数据集复现/继续训练检测模型
- 在测试集上评估模型 mAP 等指标

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L2: A computer vision project for AI teeth xray analysis. This repo features a YOLO26 object detection model trained on 
> L5: The model detects 6 classes on panoramic xrays: Prosthesis, Root Canal, caries, impaction, restoration and root stum


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `11c7873f7cab` · [字段定义](../../DATASET.md)*
