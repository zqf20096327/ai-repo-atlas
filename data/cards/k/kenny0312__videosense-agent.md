# kenny0312/videosense-agent

⭐ 29 · Python · NOASSERTION · 推送 2026-08-09 · [GitHub](https://github.com/kenny0312/videosense-agent) · 个人维护 · 中文 README

**对视频库提问并给出可播放片段与图表佐证的 AI agent**

基于 Python FastAPI 构建的 AI agent 应用：用户用自然语言对视频库提问，Gemini 2.5 模型在工具调用循环中自主决策，可调用观看视频、查询事实、语义搜索、展示片段与表格、画图、运行代码等工具，流式返回每个步骤，并以片段与图表作为回答证据；回复附带步骤、工具、耗时与费用信息。设有护栏（只读 SQL、ID 清除、请求计量）与 370 项确定性自动化评测。提供在线 demo 与本地 mock 模式运行方式，依赖 GCP 项目与 gcloud 登录访问 Gemini。许可为 Elastic License 2.0，禁止作为托管服务提供，商业许可需联系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemini 2.5 工具调用循环，流式返回每步推理
- 回答附带可播放片段、图表与费用清单（步骤/工具/秒/美元）
- 护栏：只读 SQL、ID 清除、请求计量
- 370 项确定性验证器的自动化评测，无库中内容时明确拒绝作答

## 适用场景

- 对自己的视频库用自然语言提问并获得片段佐证
- 获取带出处与数据图表的视频内容分析
- 本地 mock 模式零成本试用（无需数据库）

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L5: It watches your videos, reasons about what it sees, and answers with the clip and the chart to prove it.
> L23:  The VideoSense agent loop: a Gemini 2.5 brain decides, calls a tool, reads the result, and repeats until proven — 

## 星数曲线

```mermaid
xychart-beta
    title "kenny0312/videosense-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-31 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8ecc1bb6057c` · [字段定义](../../DATASET.md)*
