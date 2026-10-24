# VerisimilitudeX/DNAnalyzer

⭐ 185 · Java · MIT · 推送 2026-10-19 · [GitHub](https://github.com/VerisimilitudeX/DNAnalyzer) · 个人维护

**本地运行的 DNA 序列分析平台：隐私优先的基因组建模**

隐私优先的本地基因组分析平台，所有计算在用户设备完成，基因数据不出本机。功能包括密码子与蛋白编码区检测、GC 富集区与启动子元件识别、神经发育相关变异筛查、大陆祖源估计、多基因风险评分（PRS）、Smith-Waterman 序列比对（可选 PyOpenCL GPU 加速）。以 Java CLI 与 Spring Boot REST API 双形式提供，配 Web UI 与 Swagger 文档；Docker Compose 一键启动。设置 OPENAI_API_KEY 后可选生成研究者版与科普版 AI 报告，--no-ai 可跳过。声明性状预测仅供教育用途，不可用于医疗决策。由 Hack Club 501(c)(3) 财务赞助，创始人 Piyush Acharya，50 名贡献者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全本地计算，基因数据不离开设备
- 读取 FASTA/FASTQ/纯文本，输出 QC 图表、突变序列与 HTML 报告
- 23andMe/AncestryDNA 导出文件的祖源估计与逐 SNP 风险评分
- Smith-Waterman 比对支持 PyOpenCL GPU 加速，附纯 Python CPU 回退

## 适用场景

- 在本地分析自己的 DNA 测序数据而不上传第三方
- 批量脚本化处理 FASTA 文件并生成报告
- 对 23andMe/AncestryDNA 导出数据做祖源与风险评分分析

## 场景标签

 · 领域:生物信息学/基因组分析

## 证据(README 行号)

> L19: DNAnalyzer is an AI-powered, privacy-first platform for genomic analysis. All computation happens locally on your d
> L133: Pass `--no-ai` to skip the model call.

## 星数曲线

```mermaid
xychart-beta
    title "VerisimilitudeX/DNAnalyzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 184 --> 186
    line [185, 185]
```

2026-10-18 185 → 2026-10-24 185（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2a07d7d14b34` · [字段定义](../../DATASET.md)*
