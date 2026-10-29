# merdekasiberlab/xssgenai

⭐ 24 · Python · 推送 2025-11-02 · [GitHub](https://github.com/merdekasiberlab/xssgenai) · [官网](https://merdekasiber.com/xssgenai) · 组织维护

**面向现代 Web 应用的 XSS 扫描器，含 WAF 识别与可选 Gemini 分析**

命令行 XSS 扫描器，支持 SSR/SPA/混合目标，提供 quick（静态 BFS）与 deep（Playwright 爬虫）两种模式。核心机制包括七阶段 payload 引擎、DOM 动态测试与 CDP 覆盖采集、Blind XSS OAST 回调、WAF 指纹识别与绕过提示、CSP 绕过目录、GraphQL 侦察。AI 部分为可选的 Google Gemini 分析层（需 GENAI_API_KEY），基于运行时证据输出排序 sink 与缓解建议；无 AI 时扫描流程仍可运行。通过 git clone + venv + pip 依赖 + Playwright 安装使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七阶段 payload 测试引擎（header/stored/CSP-aware/coverage-guided 等）
- WAF 指纹识别与限速/绕过提示（可扩展 YAML 指纹库）
- Blind XSS OAST 多向量信标与回调轮询
- 可选 Gemini 分析层：基于 sanitiser 图谱与运行时数据生成排序 sink 与缓解建议

## 适用场景

- 对 SPA/SSR 站点执行深度 XSS 漏洞扫描与验证
- Bug Bounty 中识别 WAF 并获取绕过指引
- 通过 OAST 回调检测存储型/延迟触发的 Blind XSS
- 对 GraphQL 端点做侦察与 resolver 参数模糊测试

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L21: |AI Integration|Optional Google Gemini analysis (`GENAI_API_KEY`)|
> L31: - **Gemini Intelligence Layer** - `ai_analysis.py` builds multi-part prompts for Google GenAI, outputting ranked si
> L87: 11. **Gemini Intelligence (Optional)** - `ai_analysis` builds multi-part prompts from sanitiser maps, runtime findi

## 星数曲线

```mermaid
xychart-beta
    title "merdekasiberlab/xssgenai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `3ae3bb5cf000` · [字段定义](../../DATASET.md)*
