# tensorflow/tfjs-wechat

⭐ 578 · TypeScript · 推送 2026-06-24 · [GitHub](https://github.com/tensorflow/tfjs-wechat) · [官网](https://tensorflow.org/js) · 组织维护 · 中文 README

**微信小程序调用 TensorFlow.js 的插件封装**

封装 TensorFlow.js 库供第三方微信小程序调用的插件，通过 appid 在小程序后台添加后，以 npm/yarn 引入 tfjs 分包（core/converter/webgl/cpu 等）并配置 configPlugin 即可使用 tfjs API。支持模型 localStorage 缓存与本地文件保存（各限 10MB）、WebAssembly backend（README 注明当前因打包不兼容而损坏）、tfjs-models 模型库及谷歌中国镜像。需微信基础库 >=2.7.3、开发者工具 >=v1.02.1907022。由 TensorFlow.js 团队维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 TensorFlow.js 供第三方微信小程序调用
- 支持按需加载 tfjs 分包以适应小程序 2M 大小限制
- 模型 localStorage 缓存与本地文件保存（各 10MB 限制）
- 提供 tfjs-models 谷歌中国镜像地址供国内用户使用

## 适用场景

- 在微信小程序中运行图像识别、人体姿态识别等模型
- 中低端 Android 手机上使用 WASM backend 跑模型
- 国内网络环境下通过中国镜像加载预训练模型

## 场景标签

 · 领域:移动端机器学习/小程序开发

## 证据(README 行号)

> L3: TensorFlow.js 微信小程序插件封装了TensorFlow.js库，用于提供给第三方小程序调用。
> L2: TensorFlow.js是谷歌开发的机器学习开源项目，致力于为javascript提供具有硬件加速的机器学习模型训练和部署。

## 星数曲线

```mermaid
xychart-beta
    title "tensorflow/tfjs-wechat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 577 --> 579
    line [578, 578]
```

2026-10-18 578 → 2026-10-22 578（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `18b7de5dc221` · [字段定义](../../DATASET.md)*
