# repkovsky/aibrick

⭐ 19 · JavaScript · MIT · 推送 2026-02-22 · [GitHub](https://github.com/repkovsky/aibrick) · [官网](https://repkovsky.github.io/aibrick/) · 个人维护

**浏览器应用：用 TeachableMachine 模型为乐高轮毂做音/像识别**

面向使用 Pybricks 固件编程 Lego Mindstorms/Spike/Technic 轮毂的爱好者与教育用户：在浏览器中通过 TensorFlow.js 运行 TeachableMachine 音频/图像模型，处理摄像头/麦克风输入，识别结果（类别概率与检测事件）经 Web Bluetooth 发送到轮毂，由 aibrick.py 模块接收。模型需先在 TeachableMachine 训练并上传获取链接；所有推理在本地设备进行，仅在下载模型时需要网络。代码适配 pybricks 3.6.0，需 Chrome 浏览器与蓝牙。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器端 TensorFlow.js 运行 TeachableMachine 音频/图像模型
- 识别结果（概率帧 10Hz 与检测帧）经 Web Bluetooth 发送到轮毂
- 本地处理，不录制、不存储、不上传音频/图像
- 提供砖块分类、姿态识别示例程序

## 适用场景

- 训练图像/声音模型让乐高轮毂对物体或手势做出反应
- 课堂中演示机器学习与机器人结合
- 无需轮毂端算力即可为乐高作品添加识别能力

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: aiBrick is browser application which enables using machine learning and artificial intelligence algorithms with Lego
> L33: * aiBrick web application starts to process audio/image. Depending on the configuration it will send two types of f

## 星数曲线

```mermaid
xychart-beta
    title "repkovsky/aibrick 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `22b97a25bd41` · [字段定义](../../DATASET.md)*
