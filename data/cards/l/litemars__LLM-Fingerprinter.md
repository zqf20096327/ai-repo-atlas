# litemars/LLM-Fingerprinter

⭐ 22 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/litemars/LLM-Fingerprinter) · 个人维护

**黑盒指纹识别系统：探测未知 LLM 所属模型家族**

通过向目标模型发送 31 个分层提示（判别性/行为/风格三层），提取每层 402 维特征（句子嵌入+语言学+行为特征），经 PCA 降维后用 Random Forest+SVM+MLP 集成分类器判定模型家族（GPT、LLaMA、Mistral 等），模板分类器进一步识别具体版本，可追溯微调模型的基础模型。支持 Ollama、OpenAI、Gemini 等后端及自定义 HTTP 端点；带预训练分类器，置信度超阈值时提前停止以节省 API 调用。面向 AI 安全研究与开发者，以 PyPI 包与 CLI 形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 31 个分层提示 + 1206 维特征的黑盒指纹识别，可识别微调模型的基础家族
- 集成分类器判家族、模板分类器（余弦距离）判具体版本的两阶段识别
- 新增家族无需重训（add-family），置信度提前停止节省 API 调用
- 支持 Ollama/OpenAI/Gemini/自定义 HTTP 端点等多种后端

## 适用场景

- 黑盒环境下探测某 API 背后实际使用的模型家族
- 验证微调模型是否基于其所称的基础模型
- AI 安全研究中对模型服务做溯源与审计

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: A black-box fingerprinting system that identifies the underlying LLM model family (GPT, LLaMA, Mistral, etc.) by ana
> L28: 4. **Ensemble classification**: Random Forest (45%) + SVM (45%) + MLP (10%)
> L30: 5. **Two-stage identification**: Ensemble → model family, Template classifier → specific model version

## 星数曲线

```mermaid
xychart-beta
    title "litemars/LLM-Fingerprinter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-27 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `cfd4a46227ef` · [字段定义](../../DATASET.md)*
