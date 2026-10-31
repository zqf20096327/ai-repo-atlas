# iamgooold/phishing-link-detector-app

⭐ 14 · Java · Apache-2.0 · 推送 2026-05-15 · [GitHub](https://github.com/iamgooold/phishing-link-detector-app) · 个人维护

**检测短信钓鱼的 Android 安全应用，AI 实时分类威胁**

面向终端用户的 Android 安全应用：拦截入站短信，经 TF-IDF 向量化后发送到 Flask 后端，由 TensorFlow/Keras 神经网络推断是否为钓鱼内容，返回置信度评分并在检出威胁时即时通知，扫描结果存入本地历史。官方称全部处理本地进行，但 ML 推理经由 REST API 后端完成，后端与训练模型在另外的仓库。前端 Java/Material Design，需配置后端 URL 才能运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 入站短信实时扫描与即时威胁通知
- TF-IDF + 神经网络的钓鱼检测与置信度评分
- 扫描历史记录与误报/漏报用户反馈
- Flask REST API 后端提供 ML 推理服务

## 适用场景

- 手机收到可疑短信时获得实时钓鱼告警
- 查看历史扫描记录与威胁等级
- 通过反馈误报/漏报参与模型改进

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: *An intelligent Android application that leverages NLP and Machine Learning to detect phishing attempts in SMS mess
> L23: - AI-powered analysis using NLP and TensorFlow/Keras models
> L32: - **Intelligent Message Analysis**: Uses TF-IDF vectorization and neural networks to detect phishing patterns

## 星数曲线

```mermaid
xychart-beta
    title "iamgooold/phishing-link-detector-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `bdd6e94d9496` · [字段定义](../../DATASET.md)*
