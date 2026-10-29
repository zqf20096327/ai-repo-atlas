# Rishabh1925/foodvisionai

⭐ 22 · TypeScript · MIT · 推送 2026-02-05 · [GitHub](https://github.com/Rishabh1925/foodvisionai) · [官网](https://foodvisionai.vercel.app) · 个人维护

**上传食物图片即可识别 101 类菜品的 Web 应用**

基于 React + Flask 的食物图像识别 Web 应用：前端用 React 18/TypeScript/Vite 构建，后端 Flask 加载 Hugging Face Hub 上的 nateraw/food Vision Transformer 预训练模型（Food-101 数据集训练，约 500MB，首次运行自动下载），对上传图片（≤10MB）返回 Top 5 预测及置信度，单次预测 1-2 秒，无需 API key，处理在本地完成。面向美食博主、营养师与食谱/餐厅应用开发者，需分别启动前后端进程，建议约 2GB 内存。

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

- Vision Transformer 模型识别 101 类食物，测试集准确率约 94%
- 返回 Top 5 预测及置信度，单次预测 1-2 秒
- 无需 API key，模型自动下载，处理在本地完成
- 提供 REST API（/api/predict），支持 PNG/JPG/GIF/WebP 上传

## 适用场景

- 想知道图片里的菜是什么
- 给食谱或餐厅应用加食物识别接口
- 营养师或美食博主快速标注食物类别

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L20: - **AI-Powered Recognition** - Advanced machine learning model trained on 101 food categories
> L47: - **Model**: `nateraw/food` from Hugging Face Hub

## 星数曲线

```mermaid
xychart-beta
    title "Rishabh1925/foodvisionai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `83d806bc348b` · [字段定义](../../DATASET.md)*
