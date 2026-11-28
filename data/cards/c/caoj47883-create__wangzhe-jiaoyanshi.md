# caoj47883-create/wangzhe-jiaoyanshi

⭐ 4 · JavaScript · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/caoj47883-create/wangzhe-jiaoyanshi) · 个人维护 · 中文 README

**王者荣耀玩家的 BP/出装/数据 Android 助手，含 AI 问答**

个人开发的 Android App，以 Java WebView 壳内嵌 React/Vite 离线站点，内置 134 位英雄、900+ 克制关系、110 套阵容数据。功能覆盖 BP 推测与分路反制、针对性出装、公式化打法、名师课堂聚合。AI 部分包括端侧 sherpa-onnx 中文语音识别（离线、热词偏置）与结合本地数据的 RAG 问答（调用用户自备的 OpenAI 兼容接口，Key 仅存本机）。数据支持 GitHub Pages 热更新与 SHA-256 校验。仅 Android 6.0+，个人侧载分发，不上架商店。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端侧 sherpa-onnx 中文流式 ASR + 134 英雄热词词典，离线语音填 Ban/Pick
- 本地数据 RAG 上下文 + 用户自备 OpenAI 兼容接口的 AI 问答
- GitHub Pages manifest + SHA-256 校验的数据热更新与回滚
- BP 推测→分路反制→一键带入出装的完整链路

## 适用场景

- 开黑时用语音快速录入敌方 Ban/Pick 获取反制推荐
- 断网环境下查英雄克制关系和针对性出装
- 赛季更新后不重装 App 自动拉取新英雄/装备数据
- 接入自己的 API Key 做基于本地数据的英雄问答

## 场景标签

`RAG` `语音识别` · 领域:知识与检索

## 证据(README 行号)

> L21: 一个私人使用的 Android App（个人项目，非官方、非商业）：
> L28: - **AI 问答**：结合本地数据的 RAG 上下文，调用你自己的 OpenAI 兼容接口；
> L156: - **AI**：前端组装本地数据 RAG 上下文，交给 Java 原生层直连外部接口（绕开 WebView CORS）。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `da13b3bf61cb` · [字段定义](../../DATASET.md)*
