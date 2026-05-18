# M&A Diligence — Standard Column Set (UK)

The default schema for a buy-side target contract review under English law. Start here, then add or cut columns based on the deal. This is a starting point, not a checklist — the SPA's warranties and the request list drive what actually matters.

```yaml
schema:
  name: "M&A Diligence — Standard (UK)"
  columns:
    - id: counterparty
      label: "Counterparty"
      type: verbatim
      prompt: "Name the contracting party other than the target entity, exactly as it appears."

    - id: agreement_type
      label: "Agreement Type"
      type: classify
      options: [msa, purchase_order, licence_in, licence_out, lease, services, supply, distribution, nda, joint_venture, loan, guarantee, employment, other]
      prompt: "What kind of agreement is this?"

    - id: effective_date
      label: "Effective Date"
      type: date
      prompt: "When did this agreement become effective?"

    - id: term
      label: "Term"
      type: duration
      prompt: "What is the initial term?"

    - id: auto_renewal
      label: "Auto-Renewal"
      type: classify
      options: [none, annual, fixed_period, evergreen]
      prompt: "Does the agreement auto-renew? On what cycle?"

    - id: termination_for_convenience
      label: "Termination for Convenience"
      type: classify
      options: [none, either_party, target_only, counterparty_only]
      prompt: "Can either party terminate without cause? Who?"

    - id: termination_notice
      label: "Termination Notice Period"
      type: duration
      prompt: "How much notice is required to terminate?"

    - id: change_of_control
      label: "Change of Control"
      type: classify
      options: [silent, consent_required, consent_not_unreasonably_withheld, automatic_termination, notice_only, counterparty_right_to_terminate]
      prompt: "Does the agreement address a change of control of the target? What triggers and what happens?"

    - id: assignment
      label: "Assignment"
      type: classify
      options: [silent, consent_required, consent_not_unreasonably_withheld, freely_assignable, assignable_to_affiliates, non_assignable]
      prompt: "Can the target assign this agreement? What restrictions apply?"

    - id: exclusivity
      label: "Exclusivity / Non-Compete"
      type: classify
      options: [none, exclusive_supplier, exclusive_customer, non_compete, non_solicit, territory_restriction, most_favoured_nation]
      prompt: "Does the agreement restrict either party from competing or contracting with others?"

    - id: liability_cap
      label: "Liability Cap"
      type: currency
      prompt: "Is there a cap on liability? What is the amount or multiplier? (GBP default)"

    - id: indemnification
      label: "Indemnification / Indemnity"
      type: classify
      options: [none, mutual, target_indemnifies, counterparty_indemnifies, ip_only, third_party_claims_only]
      prompt: "Who indemnifies whom, and for what?"

    - id: governing_law
      label: "Governing Law"
      type: verbatim
      prompt: "What jurisdiction's law governs? (English / Scots / NI / other — note exactly)"

    - id: jurisdiction_courts
      label: "Jurisdiction / Courts"
      type: verbatim
      prompt: "Which courts have jurisdiction? (English High Court / Scottish courts / arbitration / other)"

    - id: dispute_resolution
      label: "Dispute Resolution"
      type: classify
      options: [litigation, arbitration_binding, arbitration_nonbinding, mediation_first, silent]
      prompt: "How are disputes resolved?"

    - id: most_favoured_nation
      label: "MFN / Pricing Protection"
      type: classify
      options: [none, mfn_pricing, price_matching, benchmarking_right]
      prompt: "Is there a most-favoured-nation or pricing protection clause?"

    - id: minimum_commitments
      label: "Minimum Purchase / Volume Commitments"
      type: currency
      prompt: "Are there minimum purchase, volume, or spend commitments? (GBP default)"

    - id: ip_ownership
      label: "IP Ownership"
      type: classify
      options: [each_owns_own, target_owns_work_product, counterparty_owns_work_product, joint, licence_only, silent]
      prompt: "Who owns intellectual property created or used under the agreement?"

    - id: confidentiality_term
      label: "Confidentiality Survival"
      type: duration
      prompt: "How long do confidentiality obligations survive termination?"

    - id: insurance_requirements
      label: "Insurance Requirements"
      type: classify
      options: [none, public_liability, professional_indemnity, cyber, employers_liability, product_liability]
      prompt: "What insurance must be maintained? (Note: 'employers liability' is statutory in the UK)"

    - id: audit_rights
      label: "Audit Rights"
      type: classify
      options: [none, counterparty_may_audit_target, target_may_audit_counterparty, mutual]
      prompt: "Does either party have audit rights?"

    - id: notices
      label: "Notice Requirements"
      type: verbatim
      prompt: "What is the notice address and method for the target?"

    - id: tupe_relevance
      label: "TUPE Relevance"
      type: classify
      options: [not_applicable, potentially_applicable_note, employees_assigned, service_provision_change]
      prompt: "Are employees or a service provision assigned under or affected by this agreement in a way that could engage TUPE on assignment or termination?"
```

## Common additions by deal type

- **Tech / IP-heavy targets (UK):** source code escrow, open source restrictions (GPL/LGPL), UKIPO filings, data rights, software licence portability on change of control
- **Healthcare / life sciences (UK):** CQC/MHRA requirements, clinical trial obligations, NHS/ICB contracts, framework agreements
- **Government contractors (UK):** Cabinet Office Guidance on contracting, OJEU/Find a Tender service procurement rules, TUPE on contract retender, security vetting (SC/DV clearance)
- **Real estate (UK):** alienation clause (licence to assign / sublet), landlord's consent, FRI lease, break clause, rent review, SDLT/LBTT liability on assignment
- **Regulated financial (UK):** FCA authorisation conditions, PRA requirements, FSMA s.203 (inducements), regulatory capital conditions

## Common cuts for a fast first pass (UK)

For a time-pressured initial screen, these 7 columns answer 80% of the early deal questions: counterparty, effective_date, term, change_of_control, assignment, termination_for_convenience, governing_law. Run those first, expand the schema once the deal team has prioritised.

## Scotland-specific additions

Where target holds Scottish property or has material Scottish business:
- **Scottish law governing:** note where Scots law applies; flag for Scottish law firm review
- **Charges over Scottish property:** check for floating charges registered at both Companies House AND the Register of Sasines / Land Register of Scotland
- **Scottish court jurisdiction:** Court of Session (Outer House — equivalent of English High Court; Inner House — equivalent of Court of Appeal)
