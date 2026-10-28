# theairbend3r/poke-zoo

⭐ 19 · JavaScript · GPL-3.0 · 推送 2026-02-28 · [GitHub](https://github.com/theairbend3r/poke-zoo) · [官网](https://pokezoo.onrender.com/) · 个人维护

**网页应用：从图片识别宝可梦并建立收藏（Tensorflow.js）**

基于 MERN 技术栈的宝可梦收藏 Web 应用：用户注册登录后可创建收藏集，通过 webcam 或上传图片识别宝可梦并加入收藏，输出 6 个最接近的匹配。深度学习部分使用在 150 类宝可梦图像数据集上微调的 MobileNet，转换为 Tensorflow.js 在浏览器中推理，支持 WebGL 加速，模型准确率 0.81。后端用 Node.js/Express 与 MongoDB，托管于 Heroku，训练流程使用 Docker + Python + Tensorflow。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 webcam 或上传图像识别 150 种宝可梦
- MobileNet 微调后转 Tensorflow.js，浏览器端推理（WebGL 加速可用）
- 识别输出 6 个最接近匹配
- 支持收藏集创建、编辑与去重约束

## 适用场景

- 拍摄或上传图片识别宝可梦
- 建立并管理个人宝可梦收藏集
- 体验浏览器端深度学习推理的 Web 应用

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L5: PokeZoo is webapp that enables users to create their own Pokemon collections by identifying Pokemon from images usin
> L48: PokeZoo has a feature to identify Pokemon from images. It is trained to identify **150** Pokemon. The model used is

## 星数曲线

```mermaid
xychart-beta
    title "theairbend3r/poke-zoo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f1140798e995` · [字段定义](../../DATASET.md)*
