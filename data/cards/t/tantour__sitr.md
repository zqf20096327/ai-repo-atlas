# tantour/sitr

⭐ — · [GitHub]() · 个人维护

**为穆斯林用户提供本地端图像/视频人物遮挡的 Chrome 扩展**

Sitr 是一个 Chrome 扩展，在本地设备上运行模型，对网页图片和视频中的选定人物施加黑块、模糊或像素化遮挡，支持按性别分别设置皮肤/头发区域或全身覆盖，界面提供英语与阿拉伯语及多种主题。安装采用 GitHub release 的解包 ZIP（内含全部模型与推理运行时，无需 Python/Node/服务器），也可用 Node.js 从源码构建。要求 Chrome 148+，模型在 WebGPU 上运行并回退到 WASM；README 声明检测可能漏检或误分类，不保证覆盖每一帧。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地端推理，无遥测、账号或推理服务器
- 支持黑块/模糊/像素化及智能衣物填充效果
- 视频支持人物剪影/边界框与运动校正，兼容 Google Meet
- BodyPix 身体区域检测与 MediaPipe Selfie 分割（可选）

## 适用场景

- 浏览网页时自动遮挡图片/视频中的人物皮肤与头发
- Google Meet 会议中对本地视图中的选定参会者做覆盖
- 按域名配置例外或暂停站点保护

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L7: Sitr is a Chrome extension that covers selected people in supported images and videos. Choose skin and hair coverage
> L119: Inference runs locally using packaged models. Sitr has no analytics, account, telemetry, or inference server. Fram

## 星数曲线

```mermaid
xychart-beta
    title "tantour/sitr 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-19 3 → 2026-11-21 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `284b29f96c0e` · [字段定义](../../DATASET.md)*
