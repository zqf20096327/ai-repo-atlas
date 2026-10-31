# AOSSIE-Org/Social-Street-Smart

⭐ 54 · Jupyter Notebook · GPL-3.0 · 推送 2026-02-11 · [GitHub](https://github.com/AOSSIE-Org/Social-Street-Smart) · [官网](https://chromewebstore.google.com/detail/social-street-smart/ddjcjpfkmcgpgpjhlmdenmionhbnpagm?hl=ml) · 组织维护

**检测网络有害内容的 Chrome 扩展：假新闻/仇恨言论/标题党识别**

Chrome 扩展加多服务后端的两层结构：前端用 React/TypeScript 构建，后端为多个 Python 检测 API（Flask/Docker Compose 运行），使用预训练模型做标题党、仇恨言论、假新闻与图像虚假信息检测；另有网页活动跟踪、网站信誉检查与新闻溯源 API。检测任务对应 5000-5004 端口的独立服务。以源码方式安装：前端 npm 构建后以未打包扩展形式载入 Chrome，后端通过 docker compose 启动。许可为 CC-BY-NC-ND 4.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标题党/仇恨言论/假新闻/图像虚假信息四类检测，各配独立预测 API
- 新闻溯源 API 与网站信誉检查
- 前端 Chrome 扩展（React/TypeScript）+ 后端 Docker Compose 部署

## 适用场景

- 浏览网页时识别标题党与仇恨言论内容
- 核查新闻真实性与来源
- 检测图像中的虚假信息

## 场景标签

 · 领域:内容安全/浏览器工具

## 证据(README 行号)

> L9: - **ML Models**: Pre-trained models for clickbait, hate speech, and fake news detection
> L13: - Clickbait detection

## 星数曲线

```mermaid
xychart-beta
    title "AOSSIE-Org/Social-Street-Smart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-31 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cc3ab48c61d8` · [字段定义](../../DATASET.md)*
